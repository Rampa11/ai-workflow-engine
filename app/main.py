from fastapi import FastAPI
from app.engine import run_workflow
from app.database import Base, engine, SessionLocal
from app.models import Workflow

Base.metadata.create_all(bind=engine)

app = FastAPI()

workflow = {
    "trigger": "new_lead",
    "condition": "status == HOT",
    "actions": ["send_email", "log"]
}

@app.post("/workflows/")
def create_workflow(data: dict):
    db = SessionLocal()

    try:
        workflow = Workflow(
            trigger=data["trigger"],
            condition=data["condition"],
            actions=",".join(data["actions"])
        )

        db.add(workflow)
        db.commit()
        db.refresh(workflow)

        return workflow

    finally:
        db.close()


@app.post("/trigger/")
def trigger_event(data: dict):
    db = SessionLocal()

    try:
        workflows = db.query(Workflow).all()

        results = []

        for workflow in workflows:
            workflow_dict = {
                "trigger": workflow.trigger,
                "condition": workflow.condition,
                "actions": workflow.actions.split(",")
            }

            result = run_workflow(workflow_dict, data)
            results.append(result)

        return {"results": results}

    finally:
        db.close()