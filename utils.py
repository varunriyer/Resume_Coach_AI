import re
from typing import Dict, List, Set

def calculate_skill_match(resume_skills: List[str], job_skills: List[str]) -> Dict:
    """Calculate skill match percentage and identify gaps."""
    # Convert lists to sets for set operations
    resume_skills_set = {s.lower() for s in resume_skills}
    job_skills_set = {s.lower() for s in job_skills}

    matching_skills = resume_skills_set.intersection(job_skills_set)
    missing_skills = job_skills_set - resume_skills_set
    extra_skills = resume_skills_set - job_skills_set

    match_percentage = len(matching_skills) / len(job_skills_set) * 100 if job_skills_set else 0

    return {
        "match_percentage": round(match_percentage, 2),
        "matching_skills": sorted(list(matching_skills)),
        "missing_skills": sorted(list(missing_skills)),
        "extra_skills": sorted(list(extra_skills))
    }

def extract_skills(text: str) -> List[str]:
    """Extract skills from text using common patterns."""
    # Common technical skills and keywords
    skill_patterns = [
        r'python|java|javascript|react|node\.js|sql|aws|docker|kubernetes|html|css',
        r'machine learning|artificial intelligence|data science|deep learning',
        r'project management|agile|scrum|leadership|team management',
        r'communication|problem solving|analytical|critical thinking'
    ]

    skills = set()
    for pattern in skill_patterns:
        matches = re.findall(pattern, text.lower())
        skills.update(matches)

    return sorted(list(skills))

def format_report(analysis: Dict) -> str:
    """Format the analysis report with proper spacing and sections."""
    report = """
    # Career Coach Analysis Report

    ## Match Score
    {match_percentage}%

    ## Matching Skills
    {matching_skills}

    ### Skills to Develop
    {missing_skills}

    ### Your Unique Strengths
    {extra_skills}

    ### Recommendations
    {recommendations}
    """.format(
        match_percentage=analysis["match_percentage"],
        matching_skills="\n- " + "\n- ".join(analysis["matching_skills"]) if analysis["matching_skills"] else "None found",
        missing_skills="\n- " + "\n- ".join(analysis["missing_skills"]) if analysis["missing_skills"] else "None found",
        extra_skills="\n- " + "\n- ".join(analysis["extra_skills"]) if analysis["extra_skills"] else "None found",
        recommendations="\n- " + "\n- ".join(analysis["recommendations"]) if analysis.get("recommendations") else "Loading recommendations..."
    )

    return report