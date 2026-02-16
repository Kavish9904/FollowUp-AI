import time
import json
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from agent_utils import extract_tasks_from_text

app = FastAPI(title="Meeting-to-Action Agent")

# CORS setup (so Streamlit or any frontend can call it later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Meeting-to-Action Agent backend is running ✅"}


@app.post("/extract_tasks")
async def extract_tasks(request: Request):

    start_time = time.time() 

    data = await request.json()
    transcript = data.get("transcript", "")

    if not transcript:
        return {"error": "No transcript provided!"}

    try:
        extracted_tasks = extract_tasks_from_text(transcript)

        # Ensure it's a list
        if not isinstance(extracted_tasks, list):
            extracted_tasks = []

        # Sort tasks by deadline if present
        extracted_tasks = sorted(
            extracted_tasks,
            key=lambda x: x.get("deadline", "")
        )

        execution_time = round(time.time() - start_time, 2)

        output_data = {
            "status": "success",
            "generated_tasks": extracted_tasks,
            "execution_time": f"{execution_time}s"
        }

        # Save to Output.json
        with open("Output.json", "w") as f:
            json.dump(output_data, f, indent=4)

        return output_data

    except Exception as e:
        return {"error": str(e)}

