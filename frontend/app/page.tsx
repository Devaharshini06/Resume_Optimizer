"use client";

import { useState } from "react";

export default function Home() {

const [file, setFile] = useState<File | null>(null);

const [jobDescription, setJobDescription] =
useState("");

const [targetRole, setTargetRole] =
useState("");

const [result, setResult] =
useState<any>(null);

const [resumeContext, setResumeContext] =
useState<any>(null);

const [coverLetter, setCoverLetter] =
useState("");

const [chatMessage, setChatMessage] =
useState("");

const [chatResponse, setChatResponse] =
useState("");

async function optimizeResume() {
if (!file) return;

const formData = new FormData();

formData.append(
  "resume",
  file
);

formData.append(
  "job_description",
  jobDescription
);

formData.append(
  "target_role",
  targetRole
);

const response = await fetch(
  "http://127.0.0.1:8000/resume/upload",
  {
    method: "POST",
    body: formData
  }
);

const data =
  await response.json();

setResult(data);
setResumeContext(data);
}

async function downloadResume() {
if (!file) return;

const formData = new FormData();

formData.append(
  "resume",
  file
);

formData.append(
  "job_description",
  jobDescription
);

formData.append(
  "target_role",
  targetRole
);

const response = await fetch(
  "http://127.0.0.1:8000/resume/download",
  {
    method: "POST",
    body: formData
  }
);

const blob =
  await response.blob();

const url =
  window.URL.createObjectURL(blob);

const a =
  document.createElement("a");

a.href = url;

a.download =
  "optimized_resume.docx";

a.click();
}

async function generateCoverLetter() {
if (!file) return;

const formData =
  new FormData();

formData.append(
  "resume",
  file
);

formData.append(
  "job_description",
  jobDescription
);

formData.append(
  "target_role",
  targetRole
);

const response =
  await fetch(
    "http://127.0.0.1:8000/cover-letter/generate",
    {
      method: "POST",
      body: formData
    }
  );

const data =
  await response.json();

setCoverLetter(
  data.cover_letter
);
}

async function sendMessage() {
const response = await fetch(
  "http://127.0.0.1:8000/chat",
  {
    method: "POST",
    headers: {
      "Content-Type":
        "application/json"
    },
    body: JSON.stringify({
      message: chatMessage,
      resume_context: resumeContext
    })
  }
);

const data =
  await response.json();

setChatResponse(
  data.response
);
}

return (
<div className="max-w-7xl mx-auto p-10">

  <h1 className="text-4xl font-bold mb-8">

    Hustle Hive

  </h1>

  <div className="border rounded-lg p-6">

    <h2 className="text-2xl font-bold mb-4">
      Resume Optimizer
    </h2>

    <input
      type="file"
      accept=".pdf"
      onChange={(e) =>
        setFile(
          e.target.files?.[0] || null
        )
      }
    />

    <textarea
      placeholder="Paste Job Description"
      className="w-full border p-3 mt-4"
      rows={10}
      value={jobDescription}
      onChange={(e) =>
        setJobDescription(
          e.target.value
        )
      }
    />

    <input
      type="text"
      placeholder="Target Role"
      className="w-full border p-3 mt-4"
      value={targetRole}
      onChange={(e) =>
        setTargetRole(
          e.target.value
        )
      }
    />

    <div className="flex flex-wrap gap-4 mt-4">

      <button
        onClick={optimizeResume}
        className="bg-black text-white px-4 py-2 rounded"
      >
        Optimize Resume
      </button>

      <button
        onClick={downloadResume}
        className="bg-green-600 text-white px-4 py-2 rounded"
      >
        Download Resume
      </button>

      <button
        onClick={generateCoverLetter}
        className="bg-blue-600 text-white px-4 py-2 rounded"
      >
        Generate Cover Letter
      </button>

    </div>

  </div>

  {result && (

    <div className="mt-10">

      <div className="grid md:grid-cols-4 gap-4">

        <div className="border rounded p-4">
          <h3 className="font-bold">
            ATS Score
          </h3>
          <p className="text-4xl">
            {result.ats_score}
          </p>
        </div>

        <div className="border rounded p-4">
          <h3 className="font-bold">
            Skill Match
          </h3>
          <p className="text-4xl">
            {result.skill_match_percentage}%
          </p>
        </div>

        <div className="border rounded p-4">
          <h3 className="font-bold">
            Matched Skills
          </h3>
          <p className="text-4xl">
            {result.matched_skills?.length}
          </p>
        </div>

        <div className="border rounded p-4">
          <h3 className="font-bold">
            Missing Skills
          </h3>
          <p className="text-4xl">
            {result.missing_skills?.length}
          </p>
        </div>

      </div>

      <div className="mt-8">

        <h2 className="text-xl font-bold">
          Resume Skills
        </h2>

        <div className="flex flex-wrap gap-2 mt-2">

          {result.resume_skills?.map(
            (skill: string) => (
              <span
                key={skill}
                className="bg-zinc-800 text-white px-3 py-1 rounded-lg border border-zinc-700"
              >
                {skill}
              </span>
            )
          )}

        </div>

      </div>

      <div className="mt-8">

        <h2 className="text-xl font-bold">
          JD Skills
        </h2>

        <div className="flex flex-wrap gap-2 mt-2">

          {result.jd_skills?.map(
            (skill: string) => (
              <span
                key={skill}
                className="bg-blue-600 text-white px-3 py-1 rounded-lg"
              >
                {skill}
              </span>
            )
          )}

        </div>

      </div>

      <div className="mt-8">

        <h2 className="text-xl font-bold text-red-600">
          Missing Skills
        </h2>

        <ul className="list-disc ml-6">

          {result.missing_skills?.map(
            (skill: string) => (
              <li key={skill}>
                {skill}
              </li>
            )
          )}

        </ul>

      </div>

      <div className="mt-8">

        <h2 className="text-xl font-bold">
          Skill Gap Analysis
        </h2>

        {result.skill_gap_analysis?.map(
          (item: any, index: number) => (

            <div
              key={index}
              className="border rounded p-4 mt-3"
            >

              <h3 className="font-bold">
                {item.skill}
              </h3>

              <p>
                Importance:
                {" "}
                {item.importance}
              </p>

              <p>
                {item.recommendation}
              </p>

            </div>

          )
        )}

      </div>

      {coverLetter && (

        <div className="mt-10">

          <h2 className="text-2xl font-bold mb-4">
            Cover Letter
          </h2>

          <pre className="whitespace-pre-wrap border rounded p-4">
            {coverLetter}
          </pre>

        </div>

      )}

    </div>

  )}

  <div className="mt-12 border rounded-lg p-6">

    <h2 className="text-2xl font-bold mb-4">

      AI Career Assistant

    </h2>

    <textarea
      value={chatMessage}
      onChange={(e) =>
        setChatMessage(
          e.target.value
        )
      }
      rows={4}
      className="w-full border p-3"
      placeholder="Ask about your resume, ATS score, internships, projects..."
    />

    <button
      onClick={sendMessage}
      className="bg-purple-600 text-white px-4 py-2 mt-4 rounded"
    >
      Send
    </button>

    {chatResponse && (

      <div className="mt-4 border rounded p-4">

        {chatResponse}

      </div>

    )}

  </div>

</div>
);
}
