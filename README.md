
# 🎥 YouTube Video Summarizer using Gemini API

This project is a web app built with **Streamlit** that extracts captions from a YouTube video and generates a summary using **Google's Gemini Pro API**. It helps users quickly understand the content of long videos by summarizing captions based on a custom prompt.


## Features

- 🔗 Paste any YouTube video URL
- 🧠 Use Google's Gemini API to summarize the video
- 💬 Custom prompt input (e.g., "Summarize this in bullet points")
- 📄 Automatically extracts captions using `yt-dlp`
- 🖼️ Clean, simple interface using Streamlit


## Tech Stack / Requirements

- Python
- Streamlit
- yt-dlp
- webvtt-py
- google-generativeai

##  Notes

- Only works with YouTube videos that have English captions
- Make sure your Gemini API key is stored in `streamlit/secrets.toml`
- That secrets file and the captions folder are ignored from GitHub for privacy

## 💡 Future Improvements

- Add multi-language caption support
- Export summaries to PDF or TXT
- Include options like "Summarize in bullets" or "Explain like I'm 5"

## 📄 Documentation

- [📘 Project Report (PDF)](docs/Project_Report.pdf)
- [▶️ Watch Project Demo Video]([https://drive.google.com/your-copied-link-here](https://drive.google.com/file/d/16R9TinazrSnzLAkieTrnaaMClF5i86vj/view?usp=drivesdk))


## 📄 License

This project is intended for educational and non-commercial use only.

Developed by Bhavya Sri as part of an academic project.


