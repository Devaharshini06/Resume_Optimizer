from docx import Document
import os


def generate_docx(
    content: str,
    filename: str
):

    os.makedirs(
        "generated_docs",
        exist_ok=True
    )

    doc = Document()

    for line in content.split("\n"):

        if line.strip():

            doc.add_paragraph(
                line
            )

    path = f"generated_docs/{filename}"

    doc.save(path)

    return path