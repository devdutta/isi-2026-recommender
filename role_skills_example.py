"""
role_skills_example.py
======================
A worked EXAMPLE of the role -> required-skills table for Module 1 (M1).

WHAT THIS IS
------------
`role_skills` is the heart of the gap calculation. For each career role it lists
the skills that role needs. In M3 we do:

        gap = (skills the role needs)  -  (skills the student already has)

...and that gap is what the recommenders search on. So this table decides what
"the right answer" even looks like. Get it sensible and everything downstream
behaves; get it sloppy and the recommendations look random.

HOW TO USE IT
-------------
1. Copy this dictionary into your notebook's M1 cell (or `import` this file).
2. Keep the roles that fit your course dataset; add/edit the rest.
3. This is a *starting point*, not a finished answer — you are expected to grow
   it. Owning your choices here is part of the report (the Data chapter).

THE 3 RULES THAT KEEP THIS TABLE SANE
-------------------------------------
1. lowercase, always.   M3 lower-cases everything before comparing, so write
   "machine learning", never "Machine Learning" or "ML".
2. spell each skill ONE way, everywhere.   If you write "data visualization"
   for one role and "data viz" for another, the code treats them as two
   different skills and the gap maths breaks. Pick a spelling, reuse it.
3. the role is CHOSEN from this table, never free-typed.   In M3 the user picks
   a role that is a KEY in this dict. (In the optional M8 UI this is a Dropdown,
   not a text box.) A typo like "data scientist" (lowercase) would silently
   match nothing.

WHERE THESE SKILLS COME FROM
----------------------------
This table is HAND-MADE — you curate it yourself, and that is THE intended
approach for this project, NOT a shortcut. It's a few lines of Python, it removes
any external dependency, and the roles you pick are part of your report. In the
report, simply note that the table is hand-curated (a large production system
would instead use a maintained skills taxonomy) — that honest framing is exactly
what examiners reward.
"""

# ---------------------------------------------------------------------------
# THE TABLE  — ~10 roles to start. Edit freely.
# (The "Data Scientist" entry is the standard worked example used across all
#  the project docs — keep its skills as-is so your examples line up.)
# ---------------------------------------------------------------------------
role_skills = {
    "Data Scientist": [
        "python",
        "statistics",
        "machine learning",
        "sql",
        "data visualization",
        "deep learning",
    ],
    "Data Analyst": ["excel", "sql", "statistics", "data visualization", "python"],
    "ML Engineer": ["python", "machine learning", "deep learning", "sql", "cloud"],
    "Data Engineer": ["python", "sql", "data wrangling", "cloud", "big data", "apis"],
    "Business Analyst": [
        "excel",
        "sql",
        "statistics",
        "data visualization",
        "communication",
    ],
    "BI Developer": ["sql", "data visualization", "excel", "statistics", "power bi"],
    "AI Researcher": [
        "python",
        "deep learning",
        "machine learning",
        "mathematics",
        "nlp",
    ],
    "Backend Developer": ["python", "sql", "apis", "cloud", "git"],
    "MLOps Engineer": ["python", "machine learning", "cloud", "docker", "mlops"],
    "NLP Engineer": [
        "python",
        "machine learning",
        "deep learning",
        "nlp",
        "statistics",
    ],
}


# ---------------------------------------------------------------------------
# OPTIONAL HELPER  — the same gap logic you'll write in M3, shown here so you
# can see the table "working". Copy it into your notebook if it helps.
# ---------------------------------------------------------------------------
def compute_gap(current_skills, target_role):
    """Return the skills `target_role` needs that the student doesn't have yet.

    Args:
        current_skills: list[str] — skills the student already has, e.g. ["python"].
        target_role:    str       — must be a KEY in `role_skills`.

    Returns:
        list[str] — the missing skills, in the order they appear in the table.

    Raises:
        KeyError — if `target_role` is not one of the table's roles.

    Example:
        >>> compute_gap(["python"], "Data Scientist")
        ['statistics', 'machine learning', 'sql', 'data visualization', 'deep learning']
    """
    if target_role not in role_skills:
        raise KeyError(
            f"'{target_role}' is not in role_skills. Pick one of: {list(role_skills)}"
        )
    have = {s.lower() for s in current_skills}
    return [s for s in role_skills[target_role] if s.lower() not in have]


# Standard worked example used across the project docs:
#   student knows ["python"], wants to be a "Data Scientist"
#   -> compute_gap(["python"], "Data Scientist") returns:
#      ['statistics', 'machine learning', 'sql', 'data visualization', 'deep learning']
