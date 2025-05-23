import streamlit as st
import base64
from pathlib import Path
import time

# Page configuration
st.set_page_config(
    page_title="Krish Chaudhary | Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Updated CSS function with proper Streamlit button styling
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    *{
        font-family: 'Inter', sans-serif;
    }

    /* Sidebar Styling */
    .css-1v3fvcr {
        background: linear-gradient(180deg, #1A1A2E 0%, #16213E 100%) !important;
        border-right: 1px solid rgba(255,255,255,0.08);
        width: 280px !important;
        padding: 1.5rem !important;
        box-shadow: 3px 0 15px rgba(0,0,0,0.3);
        overflow-y: auto;
    }

    /* Sidebar Navigation Buttons */
    .stButton > button {
        width: 100%;
        height: 50px;
        background: #ffffff !important;
        border: 2px solid #3B82F6 !important;
        color: #000000 !important;
        border-radius: 10px !important;
        font-weight: 500 !important;
        font-size: 0.95rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
        cursor: pointer !important;
        transition: all 0.4s ease !important;
        position: relative !important;
        overflow: hidden !important;
        margin-bottom: 0.75rem !important;
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        padding-left: 1.5rem !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2) !important;
        z-index: 1;
    }

    .stButton > button:hover {
        background: #ffffff !important;
        border: 2px solid #3B82F6 !important;
        color: #000000 !important;
        transform: scale(1.05) translateX(5px) !important;
        box-shadow: 0 8px 24px rgba(59, 130, 246, 0.3), 0 0 15px rgba(59, 130, 246, 0.2) !important;
    }

    .stButton > button:active {
        background: #ffffff !important;
        border: 2px solid #3B82F6 !important;
        color: #000000 !important;
        transform: scale(0.95) !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.15) !important;
    }

    .stButton > button:focus {
        outline: none !important;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.3) !important;
    }

    /* Advanced Hover Border Animation */
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(
            90deg,
            transparent,
            rgba(59, 130, 246, 0.2),
            transparent
        );
        transition: left 0.5s ease;
        z-index: -1;
    }

    .stButton > button:hover::before {
        left: 100%;
    }

    /* Ripple Effect */
    .stButton > button::after {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        background: rgba(59, 130, 246, 0.15);
        border-radius: 50%;
        transform: translate(-50%, -50%);
        transition: width 0.6s ease, height 0.6s ease;
        z-index: -1;
    }

    .stButton > button:hover::after {
        width: 300px;
        height: 300px;
    }

    /* Responsive Adjustments */
    @media (max-width: 768px) {
        .css-1v3fvcr {
            width: 220px !important;
            padding: 1rem !important;
        }

        .stButton > button {
            height: 45px !important;
            font-size: 0.9rem !important;
            padding-left: 1.2rem !important;
        }
    }

    /* Section Header Styles */
    .section-header {
        position: relative;
        font-size: 2.2rem;
        font-weight: 600;
        text-align: center;
        margin: 2rem 0 1.5rem 0;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6);
        background-clip: text;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .section-header:hover {
       transform: scale(1.05); /* Slight scale for emphasis */
       text-shadow: 0 0 8px rgba(59, 130, 246, 0.5); /* Subtle glow effect */
    }

    .section-header::after {
        content: '';
        position: absolute;
        bottom: -5px;
        left: 50%;
        transform: translateX(-50%);
        width: 80px;
        height: 3px;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6);
        border-radius: 2px;
    }
    .section-header:hover::after {
        width: 100px; /* Slightly wider underline on hover */
    }

    /* Profile Section */
    .profile-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 2rem;
    }

    .profile-card {
        position: relative;
        margin-bottom: 1rem;
    }

    .profile-img-new {
        width: 400px;
        height: 400px;
        border-radius: 50%;
        border: 3px solid transparent;
        background: linear-gradient(45deg, #667eea, #764ba2);
        padding: 3px;
        box-shadow: 0 15px 30px rgba(0,0,0,0.2);
        transition: transform 0.3s ease;
        object-fit: cover;
    }

    .profile-img-new:hover {
        transform: scale(1.03);
    }

    .status-indicator {
        display: flex;
        align-items: center;
        gap: 8px;
        background: rgba(76, 175, 80, 0.1);
        padding: 6px 14px;
        border-radius: 20px;
        border: 1px solid rgba(76, 175, 80, 0.2);
    }

    .status-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #4CAF50;
        animation: pulse 2s infinite;
    }

    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
    }

    .status-text {
        font-size: 0.85rem;
        color: #4CAF50;
        font-weight: 500;
    }

    .hero-content {
        padding: 1.5rem 0;
    }

    .greeting {
        font-size: 1.5rem;
        color: #667eea;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }

    .hero-name {
        font-size: 3.8rem;
        font-weight: 700;
        background: linear-gradient(45deg, #667eea, #764ba2);
        background-clip: text;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.8rem;
    }

    .role-container {
        margin-bottom: 1.5rem;
    }

    .role-prefix {
        font-size: 1.1rem;
        color: #5a6c7d;
        font-weight: 500;
    }

    .rotating-roles {
        position: relative;
        height: 35px;
        margin-top: 0.5rem;
    }

    .role-item {
        position: absolute;
        font-size: 1.6rem;
        font-weight: 600;
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        background-clip: text;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        opacity: 0;
        animation: roleRotate 8s infinite;
    }

    .role-item:nth-child(1) { animation-delay: 0s; }
    .role-item:nth-child(2) { animation-delay: 2s; }
    .role-item:nth-child(3) { animation-delay: 4s; }
    .role-item:nth-child(4) { animation-delay: 6s; }

    @keyframes roleRotate {
        0%, 22.5% { opacity: 1; transform: translateY(0); }
        25%, 97.5% { opacity: 0; transform: translateY(-15px); }
        100% { opacity: 0; transform: translateY(0); }
    }

    .hero-description {
        font-size: 1.1rem;
        line-height: 1.7;
        color: #5a6c7d;
        margin-bottom: 1.5rem;
    }

    .stats-section {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1rem;
        margin: 2rem 0;
        padding: 1.5rem;
        background: rgba(102, 126, 234, 0.05);
        border-radius: 12px;
    }

    .stat-card {
        text-align: center;
        padding: 1.2rem;
        background: white;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }

    .stat-card:hover {
        transform: translateY(-3px);
    }

    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(45deg, #667eea, #764ba2);
        background-clip: text;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .stat-label {
        font-size: 1.3rem;
        color: #5a6c7d;
        font-weight: 500;
    }
    @media (max-width: 768px) {
        .stats-section {
            grid-template-columns: repeat(2, 1fr); /* 2 columns for tablets */
            gap: 0.8rem;
            padding: 1rem;
            margin: 1.5rem 0;
        }

        .stat-card {
            padding: 0.8rem;
        }

        .stat-number {
            font-size: 2rem; /* Reduced for smaller screens */
        }

        .stat-label {
            font-size: 1rem; /* Reduced for better fit */
        }
    }

    @media (max-width: 480px) {
        .stats-section {
            grid-template-columns: 1fr; /* Single column for small mobile screens */
            gap: 0.6rem;
            padding: 0.8rem;
        }

        .stat-card {
            padding: 0.6rem;
        }

        .stat-number {
            font-size: 1.8rem; /* Further reduced for very small screens */
        }

        .stat-label {
            font-size: 0.9rem; /* Further reduced for readability */
        }
    }

    .social-section {
        margin: 2rem 0;
    }

    .social-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        background: linear-gradient(45deg, #667eea, #764ba2);
        background-clip: text;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .social-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 1rem;
        max-width: 600px;
        margin: 0 auto;
    }

    .social-card {
        display: flex;
        align-items: center;
        padding: 1rem;
        background: white;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        text-decoration: none;
        color: inherit;
        transition: transform 0.3s ease;
        border-left: 3px solid transparent;
    }

    .social-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.15);
    }

    .social-card.linkedin { border-left-color: #0077B5 }
    .social-card.github { border-left-color: #333; }
    .social-card.whatsapp { border-left-color: #25D366; }
    .social-card.email { border-left-color: #EA4335; }

    .social-icon {
        font-size: 2.2rem; /* Increased from 1.8rem for larger icon */
        margin-right: 0.8rem;
        width: 48px; /* Increased from 40px to accommodate larger icon */
        height: 48px; /* Increased from 40px to maintain square shape */
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 8px;
        background: rgba(102, 126, 234, 0.1);
    }

    .social-name {
        font-size: 1.5rem;
        font-weight: 600;
        color: #2c3e50;
    }

    .social-desc {
        font-size: 1.0rem;
        color: #7f8c8d;
    }

    .card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin: 1.5rem auto;
        max-width: 1000px; /* Adjust as needed */
        width: 100%; /* Ensure it takes available width up to max-width */
        display: block; /* Ensure block-level for margin: auto */
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    /* Ensure centering in parent container */
    div[data-testid="stVerticalBlock"] .card,
    div[data-testid="stHorizontalBlock"] .card,
    div.card {
        margin-left: auto !important; /* Force centering */
        margin-right: auto !important;
    }

    /* Tablets */
    @media (max-width: 768px) {
        .card {
            padding: 1rem;
            max-width: 90%;
            margin: 1rem auto !important; /* Force centering */
            width: 100%;
        }
    }

    /* Small Mobiles */
    @media (max-width: 480px) {
        .card {
            padding: 0.8rem;
            max-width: 95%;
            margin: 0.8rem auto !important; /* Force centering */
            width: 100%;
        }
    }

    .card:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.2); /* Enhanced hover shadow */
        transform: scale(1.02) translateY(-3px); /* Added slight scale for interactivity */
    }

    .card-title {
        font-size: 1.0rem;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 0.8rem;
    }

    .card-subtitle {
        font-size: 0.8rem;
        font-weight: 500;
        color: #3498db;
        margin-bottom: 0.5rem;
    }

    .card-text {
        font-size: 0.95rem;
        line-height: 1.6;
        color: #5a6c7d;
    }

    .skill-tag {
        display: inline-block;
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        padding: 6px 12px;
        border-radius: 20px;
        margin: 4px;
        font-weight: 500;
        font-size: 0.85rem;
        transition: transform 0.3s ease;
    }

    .skill-tag:hover {
        transform: scale(1.03);
    }

    .contact-form {
        background: linear-gradient(135deg, #667eea, #764ba2);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
    }

    .footer {
        text-align: center;
        padding: 1.5rem;
        background: linear-gradient(135deg, #2c3e50, #3498db);
        color: white;
        margin-top: 2rem;
        border-radius: 10px;
    }

    a.download-btn {
        background: linear-gradient(45deg, #2ecc71, #27ae60); /* Vibrant green gradient */
        color: #1a1a1a !important; /* Dark gray text with !important to override */
        padding: 10px 20px;
        border: none;
        border-radius: 20px;
        font-weight: 600;
        cursor: pointer;
        transition: transform 0.3s ease, box-shadow 0.3s ease, background 0.3s ease;
        text-decoration: none;
        display: inline-block;
    }

    a.download-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
        background: linear-gradient(45deg, #27ae60, #2ecc71); /* Subtle gradient shift */
        color: #1a1a1a !important; /* Ensure dark gray on hover */
    }

    .timeline-item {
        border-left: 2px solid #667eea;
        padding-left: 1.5rem;
        margin-bottom: 1.5rem;
        position: relative;
    }

    .timeline-item::before {
        content: '';
        position: absolute;
        left: -6px;
        top: 0;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: #667eea;
    }

    /* Responsive Adjustments */
    @media (max-width: 768px) {
        .css-1v3fvcr {
            width: 200px !important;
            padding: 0.75rem !important;
        }

        .stButton > button {
            height: 40px !important;
            font-size: 0.85rem !important;
        }

        .section-header {
            font-size: 1.8rem;
        }

        .hero-name {
            font-size: 2.5rem;
        }

        .stats-section {
            grid-template-columns: repeat(2, 1fr);
        }

        .social-grid {
            grid-template-columns: 1fr;
        }

        .profile-img-new {
            width: 400px;
            height: 400px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

def get_base64_of_bin_file(bin_file):
    """Convert binary file to base64"""
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return None

def create_download_link(file_path, link_text):
    """Create a download link for files"""
    try:
        with open(file_path, "rb") as file:
            btn = st.download_button(
                label=link_text,
                data=file,
                file_name=file_path,
                mime="application/octet-stream",
                key=f"download_{file_path}"
            )
        return btn
    except:
        return st.error(f"File {file_path} not found")


    
def home_section():
    """Home section with profile and introduction"""
    
    # Load and encode profile picture (JPG format)
    profile_pic_path = "images/profile.jpg"
    profile_pic_base64 = get_base64_of_bin_file(profile_pic_path)
    if profile_pic_base64 is None:
        st.error(f"Profile picture '{profile_pic_path}' not found. Please ensure the file exists in the images directory.")
        profile_pic_base64 = ""  # Fallback to empty string to avoid breaking the layout

    with open("resume/resume.pdf", "rb") as f:
        pdf_data = f.read()
    # Hero Section with Split Layout
    col1, col2 = st.columns([1, 2])
    
    with open("resume/resume.pdf", "rb") as f:
        pdf_data = f.read()

    with col1:
        st.markdown(f"""
        <div class="profile-container">
            <div class="profile-card">
                <img src="data:image/jpeg;base64,{profile_pic_base64}" class="profile-img-new" alt="Profile Picture">
                <div class="profile-glow"></div>
            </div>
            <div class="status-indicator">
                <div class="status-dot"></div>
                <span class="status-text">Available for opportunities</span>
            </div>
            <div style="margin-top: 1rem; display: flex; justify-content: center;">
                <a id="resume-card" href="data:application/pdf;base64,{base64.b64encode(pdf_data).decode()}" download="Krish_Chaudhary_Resume.pdf" class="download-btn">
                    📄 Download Resume
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="hero-content">
            <div class="greeting">👋 Hello, I'm</div>
            <h1 class="hero-name">Krish </br>Chaudhary</h1>
            <div class="role-container">
                <span class="role-prefix">I'm a passionate</span>
                <div class="rotating-roles">
                    <span class="role-item active">Data Analyst <span style="background: none; -webkit-text-fill-color: initial;">📊</span></span>
                    <span class="role-item">Data Scientist <span style="background: none; -webkit-text-fill-color: initial;">🔬</span></span>
                    <span class="role-item">ML Engineer <span style="background: none; -webkit-text-fill-color: initial;">🤖</span></span>
                    <span class="role-item">BI Analyst <span style="background: none; -webkit-text-fill-color: initial;">📈</span></span>
                </div>
            </div>
            <p class="hero-description">
                🌟 <strong>Data Science Enthusiast & Innovator</strong><br>
                🎓 Currently pursuing B.Tech in CSE-AI, diving deep into the world of Data Science.<br>
                🚀 Passionate about leveraging <strong>cutting-edge technologies</strong> to unlock transformative insights from data.<br>
                💻 Skilled in <strong>Machine Learning, Deep Learning, NLP, and AI</strong>, with expertise in Python, SQL, and Power BI.<br>
                📊 Proficient in crafting <strong>impactful visualizations</strong> and predictive models to drive data-informed decisions.<br>
                🧠 Srtong Knowledge in <strong>Natural Language Processing</strong> and advanced deep learning techniques for intelligent solutions.<br>
                📚 <strong>Lifelong learner</strong> dedicated to mastering emerging data science tools and techniques.<br>
                🔍 Eager to build <strong>innovative solutions</strong> that harness the power of data for real-world impact.
            </p>
        </div>
        <style>
            .rotating-roles {
                position: relative;
                height: 40px;
                margin-top: 0.5rem;
            }
            .role-item {
                position: absolute;
                font-size: 1.8rem;
                font-weight: 700;
                background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
                background-clip: text;
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                opacity: 0;
                animation: roleRotate 12s infinite;
                transition: opacity 0.5s ease;
            }
            .role-item:nth-child(1) { animation-delay: 0s; }
            .role-item:nth-child(2) { animation-delay: 3s; }
            .role-item:nth-child(3) { animation-delay: 6s; }
            .role-item:nth-child(4) { animation-delay: 9s; }
            @keyframes roleRotate {
                0%, 20% { opacity: 1; transform: translateY(0); }
                25%, 95% { opacity: 0; transform: translateY(-20px); }
                100% { opacity: 0; transform: translateY(0); }
            }
        </style>
        """, unsafe_allow_html=True)
    
    # Animated Stats Section
    st.markdown("""
    <div class="stats-section">
        <div class="stat-card">
            <div class="stat-number">2 Months+</div>
            <div class="stat-label">Expiriance</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">6+</div>
            <div class="stat-label">Projects Completed</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">5+</div>
            <div class="stat-label">Technologies</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">3+</div>
            <div class="stat-label">Certifications</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Social Links Section
    st.markdown("""
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" rel="stylesheet">

    <div class="social-section">
        <h3 class="social-title">Let's Connect & Collaborate <span style="background: none; -webkit-text-fill-color: initial;">🤝</span></h3>
        <div class="social-grid">
            <a href="https://www.linkedin.com/in/krish-chaudhary-krc8252/" target="_blank" class="social-card linkedin" >
                <div class="social-icon"><i class="fab fa-linkedin" style="color: #0A66C2;"></i></div>
                <div class="social-info">
                    <div class="social-name">LinkedIn</div>
                    <div class="social-desc">Professional Network</div>
                </div>
            </a>
            <a href="https://github.com/krish1440" target="_blank" class="social-card github">
                <div class="social-icon"><i class="fab fa-github" style="color: #333;"></i></div>
                <div class="social-info">
                    <div class="social-name">GitHub</div>
                    <div class="social-desc">Code Repository</div>
                </div>
            </a>
            <a href="https://wa.me/+916353160662" target="_blank" class="social-card whatsapp">
                <div class="social-icon"><i class="fab fa-whatsapp" style="color: #25D366;"></i></div>
                <div class="social-info">
                    <div class="social-name">WhatsApp</div>
                    <div class="social-desc">Quick Chat</div>
                </div>
            </a>
            <a href="mailto:krishchaudhary144@gmail.com" class="social-card email">
                <div class="social-icon"><i class="fas fa-envelope" style="color: #EA4335;"></i></div>
                <div class="social-info">
                    <div class="social-name">Email</div>
                    <div class="social-desc">Professional Contact</div>
                </div>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    

    
    # Hide the actual buttons and make cards clickable with custom CSS
    st.markdown("""
    <style>
    div[data-testid="column"] > div > div > div > button[key="projects_btn_hidden"],
    div[data-testid="column"] > div > div > div > button[key="contact_btn_hidden"] {
        display: none;
    }
    </style>
    
    <script>
    document.getElementById('projects-card').onclick = function() {
        document.querySelector('button[key="projects_btn_hidden"]').click();
    };
    document.getElementById('contact-card').onclick = function() {
        document.querySelector('button[key="contact_btn_hidden"]').click();
    };
    </script>
    """, unsafe_allow_html=True)

def education_section():
    """Education section with timeline style"""
    st.markdown('<h2 class="section-header">🎓 Education</h2>', unsafe_allow_html=True)
    st.markdown('<div </div>', unsafe_allow_html=True)
    st.markdown('<div </div>', unsafe_allow_html=True)
    
    # Education Card
    st.markdown("""
    <div class="card">
        <div class="timeline-item">
            <h2 class="card-title">2023 - 2027</h2>
            <h3 class="card-subtitle">Parul University </br>Vadodara, Gujrat, India </h3>
            <p style="font-weight: 600; color: #3498db;">B.Tech CSE-AI (2023 - 2027)</p>
            <p class="card-text">
                As a student at Parul University, I'm immersed in a dynamic academic environment renowned for its 
                commitment to excellence. With a focus on practical learning and cutting-edge technology, I'm building 
                a strong foundation in Computer Science with specialization in Artificial Intelligence and Machine Learning.
                The curriculum includes advanced topics in data structures, algorithms, machine learning, deep learning, 
                and artificial intelligence applications.
            </p>
        </div>
        <div class="timeline-item">
            <h2 class="card-title">2021 - 2023</h2>
            <h3 class="card-subtitle">Jawahar Navodaya Vidyalaya </br>Mehsana, Gujrat, India </h3>
            <p style="font-weight: 600; color: #3498db;">HSC (2021 - 2023)</p>
            <p class="card-text">
                As a student at Jawahar Navodaya Vidyalaya, I am immersed in a 
                vibrant and inclusive residential academic environment dedicated
                to nurturing rural talent. With a focus on holistic development 
                and high-quality education, I am building a strong foundation in 
                a CBSE-affiliated curriculum spanning sciences, mathematics, languages,
                and humanities. The program emphasizes critical thinking, experiential 
                learning, and co-curricular activities, supported by modern facilities 
                like smart classrooms and well-equipped labs, preparing me to excel in a
                competitive world while fostering national integration and social values.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)


def certifications_section():
    """Certifications section with download link inside the card"""
    st.markdown('<h2 class="section-header">🏆 Certifications</h2>', unsafe_allow_html=True)
    st.markdown('<div </div>', unsafe_allow_html=True)
    st.markdown('<div </div>', unsafe_allow_html=True)
    
    # Sample certifications - replace with your actual certifications
    certifications = [
        {
            "name": "Generative AI for Data-Driven Business Decision-Making",
            "provider": "IIM Mumbai",
            "file": "certificates/gen_ai.pdf",
            "description": "In collaboration with <strong> National Skill Development Corporation (NSDC)</strong> and <strong>CoE Logistics & Supply Chain Management IIM Mumbai Under the vision of Viksit Bharat @2047</strong> and the mission of <strong>PM GatiShakti</strong> National Master Plan"
            "Participated in a national-level program focused on applying Generative AI to enhance data-driven decision-making in business and supply chain contexts.<br> Gained hands-on experience with AI-powered tools and frameworks for business intelligence, predictive analytics, and strategic planning. <br> Explored the integration of AI in logistics and supply chain management, aligning with the objectives of <strong>India’s PM GatiShakti initiative</strong>. <br> Developed a deep understanding of how emerging AI technologies can transform data into actionable insights for efficient and scalable business operations.<br>  Contributed to the broader vision of <strong>Viksit Bharat @2047</strong>, promoting innovation and digital transformation across critical sectors."
        },
        {
            "name": "IBM Data Analyst Professional Certificate",
            "provider": "Coursera-IBM",
            "file": "certificates/IBM.pdf",
            "description": "<strong>Data Analysis :</strong>Fundamentals Understanding the data analytics process, data structures, and the roles of data professionals.<br>"
                            "<strong>Excel :</strong>Excel Performing basic to advanced spreadsheet tasks, including data entry, formulas, pivot tables, and data visualization.<br>"

                             "<strong>Python :</strong>Python Utilizing libraries like Pandas and NumPy for data manipulation and analysis.<br>"

                               "<strong>SQL :</strong>SQL Querying databases to extract and analyze data.<br>"

                                "<strong>IBM Cognos Analytics :</strong>IBM Cognos Analytics Creating interactive dashboards and visualizations to communicate data insights.<br>"

                                "<strong>Generative AI Tools :</strong>Generative AI Tools Exploring how AI can enhance data analysis processes.<br>"
        },
        {
            "name": "Data Analytics and Visualization Job Simulation",
            "provider": "Forage-accenture",
            "file": "certificates/accenture.pdf",
            "description": "Completed a virtual job simulation focused on data analytics and visualization, designed by Accenture through Forage."
            "Analyzed a large dataset to identify trends, patterns, and key insights relevant to a client’s business performance."
            "Created a <strong>comprehensive dashboard</strong> using Microsoft Excel and data visualization tools to present actionable recommendations."
            "Applied storytelling techniques to effectively communicate data-driven insights to non-technical stakeholders."
            "Gained experience in handling <strong>client-centric analytical</strong> challenges, replicating real-world consulting scenarios."
        }
        
    ]
    
    for cert in certifications:
        # Generate base64-encoded data URI for the certificate file
        try:
            with open(cert['file'], "rb") as file:
                file_data = file.read()
                base64_encoded = base64.b64encode(file_data).decode()
                file_href = f"data:application/pdf;base64,{base64_encoded}"
                file_name = cert['file'].split('/')[-1]  # Extract file name for download
        except FileNotFoundError:
            file_href = "#"  # Fallback to avoid breaking the layout
            file_name = cert['file']
            error_message = f"Certificate file '{cert['file']}' not found"
        except Exception as e:
            file_href = "#"
            file_name = cert['file']
            error_message = f"Error accessing certificate file: {str(e)}"
        else:
            error_message = None
        
        # Render the card with the downloadable link
        st.markdown(f"""
        <div class="card">
            <h3 class="card-title">{cert['name']}</h3>
            <h4 class="card-subtitle">Provided by: {cert['provider']}</h4>
            <p class="card-text">{cert['description']}</p>
            <div style="margin-top: 1rem;">
                <a class="download-btn" href="{file_href}" download="{file_name}">
                    📜 Download Certificate
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Display error message if file access failed
        if error_message:
            st.error(error_message)

def skills_section():
    """Skills section with categorized skill boxes"""
    st.markdown('<h2 class="section-header">⚡ Skills</h2>', unsafe_allow_html=True)
    st.markdown('<div </div>', unsafe_allow_html=True)
    st.markdown('<div </div>', unsafe_allow_html=True)
    
    skills_data = {
        "Programming Languages": [
            "Python", "Java", "C", "HTML", "CSS", "JavaScript"
        ],
        "Data Science & ML": [
            "Pandas", "NumPy", "Scikit-learn", "TensorFlow", "Keras",
            "Matplotlib", "Seaborn", "XGBoost", "LightGBM", "CatBoost",
            "NLTK", "SpaCy", "Transformers", "OpenCV", "Statsmodels"
        ],
        "Data Analysis & BI Tools": [
            "Power BI", "Tableau", "Excel", "Advanced Excel", "Google Sheets",
            "IBM Cognos", "Looker"
        ],
        "Development Environments": [
            "Git", "Docker", "VS Code", "Jupyter", "Spyder", "PyCharm",
            "Anaconda", "Eclipse", "Colab","mlflow"
        ],
        "Databases & DBMS": [
            "MySQL", "PostgreSQL", "MongoDB", "SQLite", "Oracle DB",
            "Snowflake", "Google BigQuery", "Amazon Redshift"
        ],
        "Cloud Platforms": [
            "AWS", "Google Cloud", "Azure", "Heroku"
        ],
        "Other Skills": [
            "Business Analysis", "Data Analysis", "Customer Acquisition",
            "Time Series Forecasting", "Big Data Processing", "ETL Pipelines"
        ],
        "Soft Skills": [
            "Analytical Thinking", "Problem Solving", "Communication",
            "Team Collaboration", "Team Leadership", "Project Management",
            "Storytelling with Data", "Stakeholder Engagement"
        ]
    }

    cols = st.columns(2)
    
    for i, (category, skills) in enumerate(skills_data.items()):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="card">
                <h3 class="card-title">{category}</h3>
                <div>
                    {''.join([f'<span class="skill-tag">{skill}</span>' for skill in skills])}
                </div>
            </div>
            """, unsafe_allow_html=True)

def projects_section():
    """Projects section"""
    st.markdown('<h2 class="section-header">🚀 Projects</h2>', unsafe_allow_html=True)
    st.markdown('<div </div>', unsafe_allow_html=True)
    st.markdown('<div </div>', unsafe_allow_html=True)
    
    # Sample projects - replace with your actual projects
    projects = [
        {
            "name": "<strong>OEA-OrderEasy-Analytics</strong>",
            "github": "https://oea-ordereasy-analytic.streamlit.app/",
            "description": "🚀 <strong>Smart Order Management System</strong> built using Streamlit to streamline order processing, tracking, and analytics for businesses.<br>"
                   "🗄️ Integrated with <strong>Supabase</strong> (PostgreSQL) for secure database management and <strong>Cloudinary</strong> for e-way bill (PDF/image) storage.<br>"
                   "🧾 <strong>Key Features:</strong><br>"
                   "• 📋 Order creation, editing, deletion, and status tracking<br>"
                   "• 📎 E-way bill upload, download, and replacement<br>"
                   "• 📊 <strong>Advanced analytics</strong>: Revenue trends, top products/customers, CLV, retention, RFM segmentation, and sales forecasting<br>"
                   "• 👤 <strong>User authentication</strong> with admin panel for managing users<br>"
                   "• 📤 Exportable Excel reports for orders and revenue summaries<br>"
                   "• 🧭 Responsive UI with sidebar navigation and expandable order details<br>"
                   "🔧 <strong>Tech Stack:</strong> Streamlit, Python, Supabase, Cloudinary, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn<br>"
                   "☁️ Deployed on <strong>Streamlit Cloud</strong> with .env-based configuration for secure keys and credentials."
        },
        {
            "name": "<strong>Handwritten Digits Classification</strong><strong>",
            "github": "https://github.com/krish1440/Hand_Digit_Classification",
            "description": "🧠 <strong>Web-based application</strong> for recognizing handwritten digits (0–9) using a deep learning model trained on the <strong>MNIST</strong> dataset.<br>"
                   "🎨 Users draw digits on an interactive canvas, and the model predicts the digit with <strong>confidence scores</strong> and <strong>probability distribution</strong>.<br>"

                   "🧾 <strong>Features:</strong><br>"
                   "• 🖌️ Interactive drawing canvas for input<br>"
                   "• ✅ Predict button to classify digits<br>"
                   "• ❌ Clear button to reset the canvas<br>"
                   "• 📈 Displays predicted digit with confidence percentage<br>"
                   "• 📊 Shows probability distribution for digits 0–9<br>"
                   "• 📱 Responsive design for both desktop and mobile<br>"

                   "🛠️ <strong>Tech Stack:</strong><br>"
                   "• 🧑‍💻 <strong>Frontend:</strong> HTML, CSS, JavaScript<br>"
                   "• 🔙 <strong>Backend:</strong> Flask (Python)<br>"
                   "• 🤖 <strong>Deep Learning:</strong> TensorFlow/Keras trained on MNIST dataset<br>"
        },
        {
            "name": "<strong>Loan status prediction</strong>",
            "github": "https://github.com/krish1440/Loan_status_prediction",
            "description": "🔍 <strong>Machine learning-powered web application</strong> and API to predict loan approval outcomes based on applicant and loan details.<br>"
                   "Designed to assist banks and financial institutions in making faster and more reliable loan eligibility decisions.<br>"

                   "🧾 <strong>Features (Web App):</strong><br>"
                   "• 🖥️ Intuitive web interface for entering applicant information<br>"
                   "• 🧠 Backend powered by a <strong>pretrained ML model</strong> for real-time predictions<br>"
                   "• 📊 Visual tools to explore loan trends and insights<br>"
                   "• ☁️ <strong>Deployed on Render</strong> for easy access and scalability<br>"

                   "🔗 <strong>Features (RESTful API):</strong><br>"
                   "• ⚙️ Predict loan approval status via a <strong>production-ready API</strong><br>"
                   "• 🔣 Handles both categorical and numerical inputs efficiently<br>"
                   "• 🧩 Easily integratable into other applications or services<br>"

                   "🛠️ <strong>Tech Stack:</strong><br>"
                   "• 🐍 Python, Flask for backend<br>"
                   "• 🤖 Scikit-learn for ML model training and inference<br>"
                   "• 🧪 Pandas, NumPy for data preprocessing<br>"
                   "• 🌐 HTML, CSS, JavaScript for the frontend<br>"
                   "• 🚀 Render for deployment<br>"
        },
        {
            "name": "<strong>Crop-Production-Analysisn</strong>",
            "github": "https://github.com/krish1440/Crop-Production-Analysis-",
            "description": "📊 <strong>Data-driven analytics platform</strong> for evaluating and visualizing crop production trends across regions in India.<br>"
                   "Developed during an internship at <strong>iNeuron Intelligence Pvt Ltd</strong> to aid agricultural decision-making through insights on productivity, regional performance, and crop trends.<br>"

                   "🔍 <strong>Key Features:</strong><br>"
                   "• 🧹 Rigorous <strong>data cleaning and validation</strong> to ensure dataset accuracy<br>"
                   "• 📐 <strong>Standardization</strong> of units and formatting for time-series analysis<br>"
                   
                   "• 📈 Enriched data with calculated <strong>productivity metrics (Production/Area)</strong> and crop categorization<br>"
                   "• 🧠 Analysis using <strong>Python (Pandas, NumPy)</strong> and visual dashboards built in <strong>Power BI</strong><br>"
                   "• 🌍 Regional insights through added 'Region' tagging for geographic analysis<br>"

                   "🛠️ <strong>Tech Stack:</strong><br>"
                   "• 🐍 Python (Pandas, NumPy) for data preprocessing and statistical analysis<br>"
                   "• 📊 Power BI for interactive dashboards<br>"

                   "🧾 <strong>Deliverables:</strong><br>"
                   "• 📄 Project Report with methodology and key insights<br>"
                   "• 🧠 HLD/LLD documentation outlining system and data flow<br>"
                   "• 🧭 Architecture diagram for visualizing processing pipeline<br>"
                   "• 🎥 Demo video showcasing features and findings<br>"

                   "🌟 <strong>Key Insights:</strong><br>"
                   "• 💰 Identification of profitable crops (e.g., wheat, maize, soybean)<br>"
                   "• 🌍 Highlighted top-producing states (Uttar Pradesh, Maharashtra, etc.)<br>"
                   "• 📈 Detected production growth trends and productivity disparities<br>"
                   "• 📍 Mapped crop performance regionally to guide resource allocation<br>"
        },
        {
            "name": "<strong>Accenture-Social-Buzz-Forage</strong>",
            "github": "https://github.com/krish1440/Accenture-Social-Buzz-Forage",
            "description": "🌟 <strong>Virtual internship project</strong> focused on leveraging social media analytics to generate actionable business insights.<br>"

                   "🔍 <strong>Project Overview:</strong><br>"
                   "Analyze social media data to understand brand sentiment, customer engagement, and trending topics.<br>"
                   "Develop dashboards and reports to visualize social buzz.<br>"

                   "✨ <strong>Key Tasks & Features:</strong><br>"
                   "• 📈 Perform sentiment analysis and trend detection from social media feeds.<br>"
                   "• 🧰 Use data visualization tools to create impactful dashboards.<br>"
            
                   "🛠️ <strong>Tech Stack & Skills:</strong><br>"
                   "• 🐍 Python (Pandas, NLTK) for data processing and sentiment analysis<br>"
                   "• 📊 Tableau / Power BI for dashboard creation<br>"
        },
        {
            "name": "<strong>Student Managment Systerm</strong>",
            "github": "https://github.com/krish1440/STUDENT_GRADE",
            "description": "📚 <strong>Comprehensive program</strong> to efficiently manage student records with easy-to-use data handling and CSV integration.<br>"

                   "✨ <strong>Features:</strong><br>"
                   "• ➕ <strong>Add Student Data:</strong> Quickly add new students with details like name, ID, age, subjects, marks, and credit points.<br>"
                   "• ✏️ <strong>Update Student Data:</strong> Modify existing student info to keep records accurate.<br>"
                   "• 🗑️ <strong>Delete Student Data:</strong> Remove student entries when needed (use cautiously!).<br>"
                   "• 👁️ <strong>Display Student Data:</strong> View detailed information for individual students or the full list.<br>"
                   "• 💾 <strong>Save to CSV:</strong> Store all student data in CSV files for persistence and future access.<br>"
        }
    ]
    
    for project in projects:
        st.markdown(f"""
        <div class="card">
            <h3 class="card-title">{project['name']}</h3>
            <p class="card-text">{project['description']}</p>  
                <a href="{project['github']}" target="_blank" class="download-btn">
                    🔗 View on github
                </a>
        </div>
        """, unsafe_allow_html=True)

def experience_section():
    """Experience section with download link inside the card"""
    st.markdown('<h2 class="section-header">💼 Experience</h2>', unsafe_allow_html=True)
    st.markdown('<div </div>', unsafe_allow_html=True)
    st.markdown('<div </div>', unsafe_allow_html=True)
    
    # Sample experiences - replace with your actual experiences
    experiences = [
        {
            "company": "INeuron Intelligence Pvt Ltd",
            "position": "Data Analyst Intern</br>Remote",
            "period": "June 2024 - July 2024",
            "certificate": "experience/ineuron_certificate.pdf",
            "description": "🌾 Led a <strong>Crop Production Analysis project</strong> analyzing a dataset of over 240,000 rows from 1997–2015, using <strong>Python</strong> libraries (Pandas, NumPy, Matplotlib, Seaborn) for data preprocessing and visualization.<br>"
                "🧹 Performed extensive <strong>data preprocessing</strong>, handling 3,730 null values, removing outliers (e.g., zero production rows), and standardizing crop names (e.g., merging synonyms like Paddy to Rice) to ensure data quality.<br>"
                "📊 Developed <strong>interactive Power BI dashboards</strong> to visualize crop production trends across seasons (Kharif, Rabi, Whole Year), states, and zones, enabling stakeholders to identify key agricultural insights.<br>"
                "🔍 Uncovered <strong>critical insights</strong>, including coconut’s 92% production dominance, leading to separate dataset analyses for balanced visualization of other crops like Rice, Wheat, and Pulses.<br>"
                "📈 Contributed to <strong>High-Level Design (HLD) and Low-Level Design (LLD)</strong> documentation, wireframes, and architecture, enhancing project planning.<br>"
                "🤝 Strengthened <strong>project management</strong> and skills, adhering to industry standards and delivering a comprehensive video presentation of findings."
        },
        {
            "company": "Abhay Engineering",
            "position": "Buisness Analyst Intern",
            "period": "April 2025 - May 2024",
            "certificate": "experience/ineuron_certificate.pdf",
            "description": "🚀 Developed <strong>OrderEasy Analytics</strong>, a Streamlit-based app for MSMEs, automating <strong>order creation</strong> and <strong>delivery tracking</strong> with real-time status and payment updates, reducing operational errors by <strong>90%</strong>.<br>"
        "📊 Designed <strong>interactive dashboards</strong> leveraging <strong>RFM analysis</strong>, <strong>Customer Lifetime Value (CLV)</strong>, and <strong>sales forecasting</strong>, boosting customer retention by <strong>20%</strong> and revenue by <strong>35%</strong>.<br>"
        "☁️ Implemented <strong>cloud-based storage</strong> for e-way bills and delivery documents, cutting document retrieval time by <strong>40%</strong> and ensuring regulatory compliance.<br>"
        "📈 Created <strong>customizable Excel reports</strong> for orders, deliveries, and revenue, filtered by status or date, enabling efficient <strong>business planning</strong>.<br>"
        "🔍 Conducted <strong>trend analysis</strong> to forecast demand and optimize <strong>business scalability</strong>, enhancing operational workflows.<br>"
        "💸 Integrated <strong>real-time payment tracking</strong> with GST calculations, improving financial transparency and reducing payment disputes by <strong>85%</strong>.<br>"
        "📋 Streamlined <strong>document management</strong> by enabling secure uploads of e-way bills and proofs, enhancing <strong>audit readiness</strong> by <strong>50%</strong>.<br>"
        "📦 Performed <strong>product performance analysis</strong>, driving <strong>inventory optimization</strong> and reducing stockouts by <strong>30%</strong>.<br>"
        "💡 Built <strong>customer segmentation models</strong> using RFM metrics, enabling targeted marketing strategies that increased engagement by <strong>25%</strong>.<br>"
        "🤝 Collaborated with <strong>cross-functional teams</strong> to drive <strong>data-driven strategies</strong>, fostering growth and operational excellence."
        }
    ]
    
    for exp in experiences:
        # Generate base64-encoded data URI for the certificate file
        try:
            with open(exp['certificate'], "rb") as file:
                file_data = file.read()
                base64_encoded = base64.b64encode(file_data).decode()
                file_href = f"data:application/pdf;base64,{base64_encoded}"
                file_name = exp['certificate'].split('/')[-1]  # Extract file name for download
        except FileNotFoundError:
            file_href = "#"  # Fallback to avoid breaking the layout
            file_name = exp['certificate']
            error_message = f"Certificate file '{exp['certificate']}' not found"
        except Exception as e:
            file_href = "#"
            file_name = exp['certificate']
            error_message = f"Error accessing certificate file: {str(e)}"
        else:
            error_message = None
        
        # Render the card with the downloadable link 
            st.markdown(f"""
            <div class="card">
                <div class="timeline-item">
                    <h3 class="card-title">{exp['company']}</h3>
                    <h4 class="card-subtitle">{exp['position']}</h4>
                    <p style="font-weight: 600; color: #3498db;">{exp['period']}</p>
                    <p class="card-text">{exp['description']}</p>
                    <div style="margin-top: 1rem;">
                        <a class="download-btn" href="{file_href}" download="{file_name}">
                            📜 Download Certificate
                        </a>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Display error message if file access failed
        if error_message:
            st.error(error_message)


def main():
    """Main function to run the portfolio with enhanced sidebar navigation"""
    
    # Load custom CSS
    load_css()
    
    # Initialize session state
    if 'current_section' not in st.session_state:
        st.session_state.current_section = 'Home'
    
    # Sidebar Navigation
    with st.sidebar:
        st.markdown('<div class="sidebar-container">', unsafe_allow_html=True)
        sections = ['Home', 'Education', 'Certifications', 'Skills', 'Projects', 'Experience']
        
        for section in sections:
            # Add active class wrapper for current section
            if st.session_state.current_section == section:
                st.markdown("""
                    <div class="nav-active">
                        <style>
                            .nav-active .stButton > button {
                                background: #ffffff !important;
                                border: 2px solid #3B82F6 !important;
                                color: #000000 !important;
                                padding: 0.5rem 1rem !important;
                                position: relative;
                                overflow: hidden;
                                transition: all 0.3s ease;
                                outline: none;
                            }
                            .nav-active .stButton > button:hover {
                                background: #ffffff !important;
                                border: 2px solid #3B82F6 !important;
                                color: #000000 !important;
                                box-shadow: 0 6px 20px rgba(0,0,0,0.25) !important;
                                transform: translateX(5px) !important;
                            }
                            .nav-active .stButton > button:active {
                                background: #ffffff !important;
                                border: 2px solid #3B82F6 !important;
                                color: #000000 !important;
                                transform: scale(0.95) !important;
                                box-shadow: 0 2px 8px rgba(0,0,0,0.15) !important;
                            }
                            .nav-active .stButton > button::after {
                                content: '';
                                position: absolute;
                                top: 0;
                                left: -100%;
                                width: 100%;
                                height: 100%;
                                background: linear-gradient(
                                    90deg,
                                    transparent,
                                    rgba(255, 255, 255, 0.2),
                                    transparent
                                );
                                animation: shine 2s infinite;
                            }
                            @keyframes shine {
                                0% { left: -100%; }
                                50% { left: 100%; }
                                100% { left: 100%; }
                            }
                        </style>
                    </div>
                """, unsafe_allow_html=True)
            
            if st.button(section, key=f"nav_{section}"):
                st.session_state.current_section = section
                st.rerun()
            
            if st.session_state.current_section == section:
                st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Display selected section
    if st.session_state.current_section == 'Home':
        home_section()
    elif st.session_state.current_section == 'Education':
        education_section()
    elif st.session_state.current_section == 'Certifications':
        certifications_section()
    elif st.session_state.current_section == 'Skills':
        skills_section()
    elif st.session_state.current_section == 'Projects':
        projects_section()
    elif st.session_state.current_section == 'Experience':
        experience_section()
    
    # Footer
    st.markdown("""
    <div class="footer">
        <p><strong>Krish Chaudhary | All Rights Reserved - 2025</strong></p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == '__main__':
    main()
