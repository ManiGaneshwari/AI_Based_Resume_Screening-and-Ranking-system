# **AI-Based Resume Screening and Ranking System**

Welcome to the **AI-Based Resume Screening and Ranking System**! This is a simple tool that helps you rank resumes based on how well they match a job description. You type in a **job description**, upload some resumes (in **PDF format**), and the system will tell you which resumes are the best fit, sorted from highest to lowest match.

---

## **How Does It Work?**

The tool uses **TF-IDF** (a way to measure how important words are) and **cosine similarity** (a way to compare text) to figure out how close each resume is to the job description.

---

## **Technologies Used**
- **Python**: Programming language.
- **Pillow**: Handles images.
- **Streamlit**: Builds the web app.
- **Pandas**: Manages data tables.
- **PyPDF2**: Reads PDF files.
- **Scikit-learn**: Analyzes text (TF-IDF and cosine similarity).

---

## **Setup**
1. Install **Python** from [python.org](https://www.python.org/downloads/).
2. Save the code as `resume_screener.py`.
3. In terminal, go to the folder and run


---

## **How to Use**
1. Run `streamlit run resume_screener.py` in terminal.
2. In the browser:
- Enter a **job description**.
- Upload **PDF resumes**.
- See the ranked list.

---

## **Example**
Job: “Python developer, 2 years experience.”  
Output:  
| Resume      | Score |  
|-------------|-------|  
| resume2.pdf | 0.85  |  
| resume1.pdf | 0.62  |  

---

## **Tips**
- Missing libraries? Re-run the `pip install` command.
- Add your own `bg.jpg` or remove the image code.



## **Output**
![Screenshot of Resume Screener](https://github.com/ManiGaneshwari/AI_Based_Resume_Screening-and-Ranking-system/blob/main/Screenshot%20(61).png)

Enjoy ranking resumes!
