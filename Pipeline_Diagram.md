# Project Pipeline Diagram

Three files in this folder:

| File | Use |
|------|-----|
| **`Project_Pipeline.png`** | **Ready-to-use image** — drop straight into a slide or screen-share in Teams. Regenerated 18 Jun 2026 from the HTML below. |
| **`Project_Pipeline.html`** | **Editable source (canonical)** — open in a browser, edit boxes/text, then re-screenshot the `.canvas` element to refresh the PNG. On-brand with the Handbook + Build Spec. |
| **`Project_Pipeline.excalidraw`** | Older editable source (excalidraw.com or the VS Code "Excalidraw" extension). The HTML is now the source of truth. |

> The **PNG is the reliable image**; the **`.html` is the reliable editable source** (the Excalidraw hand-drawn web-font didn't always render text headless).

## What it shows (top → bottom)
1. **Course dataset + role-skills** (pandas · load)
2. → **Clean & prepare** (tidy data · build the text column)
3. → **Compute skill gap** (role needs − current skills)
4. → branches into the **two recommenders**: TF-IDF (scikit-learn) and Embeddings (sentence-transformers)
5. → both feed **Evaluate & compare** (precision@k, charts)
6. → **Pick best recommender**
7. → **LLM roadmap** (Groq, free) + an **optional demo UI** — ipywidgets or Streamlit (dashed)

The recommenders + evaluation are highlighted as the **data-science core — the graded part**. Everything runs in one Jupyter notebook on Google Colab. Maps to Modules M1–M8 in the Build Specification.
