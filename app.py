import streamlit as st

st.set_page_config(
    page_title="MaskGuard AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

:root {
    --neon: #00ff88;
    --neon-dim: #00cc6a;
    --accent: #ff3366;
    --accent2: #ffcc00;
    --bg-dark: #080c14;
    --bg-card: #0d1321;
    --bg-card2: #111827;
    --border: rgba(0,255,136,0.15);
    --text: #e8f0fe;
    --text-muted: #6b7fa3;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--bg-dark) !important;
    color: var(--text) !important;
}

/* Hide streamlit default elements */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 2rem 2rem 2rem !important; max-width: 1400px !important; }

/* Animated grid background */
.stApp {
    background-color: var(--bg-dark) !important;
    background-image:
        linear-gradient(rgba(0,255,136,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,255,136,0.03) 1px, transparent 1px);
    background-size: 40px 40px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #080c14 0%, #0a1020 100%) !important;
    border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] * { color: var(--text) !important; }

/* Radio buttons */
[data-testid="stSidebar"] .stRadio label {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.95rem !important;
    padding: 10px 14px !important;
    border-radius: 8px !important;
    transition: all 0.2s !important;
    cursor: pointer !important;
}
[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(0,255,136,0.08) !important;
    color: var(--neon) !important;
}

/* Metric cards */
[data-testid="metric-container"] {
    background: var(--bg-card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    padding: 1.2rem !important;
}
[data-testid="metric-container"] label {
    color: var(--text-muted) !important;
    font-size: 0.78rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.1em !important;
}
[data-testid="metric-container"] [data-testid="stMetricValue"] {
    color: var(--neon) !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 2rem !important;
    font-weight: 700 !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, var(--neon), var(--neon-dim)) !important;
    color: #080c14 !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    letter-spacing: 0.05em !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.6rem 2rem !important;
    transition: all 0.2s !important;
    text-transform: uppercase !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(0,255,136,0.3) !important;
}

/* File uploader */
[data-testid="stFileUploader"] {
    background: var(--bg-card) !important;
    border: 2px dashed var(--border) !important;
    border-radius: 12px !important;
    padding: 1rem !important;
}

/* Success / error / warning */
.stSuccess {
    background: rgba(0,255,136,0.08) !important;
    border: 1px solid rgba(0,255,136,0.3) !important;
    border-radius: 10px !important;
    color: var(--neon) !important;
}
.stError {
    background: rgba(255,51,102,0.08) !important;
    border: 1px solid rgba(255,51,102,0.3) !important;
    border-radius: 10px !important;
}
.stWarning {
    background: rgba(255,204,0,0.08) !important;
    border: 1px solid rgba(255,204,0,0.3) !important;
    border-radius: 10px !important;
}
.stInfo {
    background: rgba(0,255,136,0.05) !important;
    border: 1px solid rgba(0,255,136,0.2) !important;
    border-radius: 10px !important;
}

/* Images */
[data-testid="stImage"] img {
    border-radius: 12px !important;
    border: 1px solid var(--border) !important;
}

/* Spinner */
.stSpinner { color: var(--neon) !important; }

/* Divider */
hr { border-color: var(--border) !important; }

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    background: var(--bg-card) !important;
    border-radius: 10px !important;
    padding: 4px !important;
    gap: 4px !important;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 8px !important;
    color: var(--text-muted) !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 600 !important;
}
.stTabs [aria-selected="true"] {
    background: rgba(0,255,136,0.15) !important;
    color: var(--neon) !important;
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding: 1.5rem 0 1rem 0; text-align: center;">
        <div style="font-size: 3rem; margin-bottom: 0.5rem;">🛡️</div>
        <div style="font-family: 'Syne', sans-serif; font-size: 1.4rem; font-weight: 800;
                    color: #00ff88; letter-spacing: 0.05em;">MASKGUARD</div>
        <div style="font-size: 0.75rem; color: #6b7fa3; letter-spacing: 0.15em;
                    text-transform: uppercase; margin-top: 2px;">AI Detection System</div>
    </div>
    <hr style="border-color: rgba(0,255,136,0.15); margin: 0.5rem 0 1.5rem 0;">
    """, unsafe_allow_html=True)

    page = st.radio(
        "NAVIGATE",
        ["🏠  Home", "📷  Live Webcam", "🖼️  Upload Image", "📊  Dashboard"],
        label_visibility="visible"
    )

    st.markdown("""
    <hr style="border-color: rgba(0,255,136,0.15); margin: 1.5rem 0 1rem 0;">
    <div style="padding: 1rem; background: rgba(0,255,136,0.05);
                border: 1px solid rgba(0,255,136,0.15); border-radius: 10px;
                font-size: 0.78rem; color: #6b7fa3; line-height: 1.7;">
        <div style="color: #00ff88; font-family: 'Syne', sans-serif;
                    font-weight: 700; margin-bottom: 0.5rem; font-size: 0.8rem;
                    text-transform: uppercase; letter-spacing: 0.1em;">Tech Stack</div>
        🧠 TensorFlow + MobileNetV2<br>
        👁️ OpenCV Face Detection<br>
        🌐 Streamlit Web UI<br>
        📦 7,553 training images
    </div>
    """, unsafe_allow_html=True)

# ── Pages ──────────────────────────────────────────────────────────────────────
if "🏠" in page:
    st.markdown("""
    <div style="padding: 3rem 0 2rem 0;">
        <div style="font-family: 'Syne', sans-serif; font-size: 0.8rem; font-weight: 600;
                    color: #00ff88; letter-spacing: 0.2em; text-transform: uppercase;
                    margin-bottom: 0.8rem;">Computer Vision Project</div>
        <h1 style="font-family: 'Syne', sans-serif; font-size: clamp(2.5rem, 6vw, 4.5rem);
                   font-weight: 800; color: #e8f0fe; line-height: 1.1; margin: 0 0 1rem 0;">
            Real-Time Face<br>
            <span style="color: #00ff88;">Mask Detection</span>
        </h1>
        <p style="font-size: 1.1rem; color: #6b7fa3; max-width: 560px; line-height: 1.7;
                  margin: 0 0 2.5rem 0;">
            An AI-powered system that detects face masks in real-time using deep learning.
            Built with MobileNetV2 transfer learning and trained on 7,553 images.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Stats row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Model Accuracy", "97%", "+42% from baseline")
    with col2:
        st.metric("Training Images", "7,553", "2 classes")
    with col3:
        st.metric("Inference Speed", "~30ms", "per frame")
    with col4:
        st.metric("Epochs Trained", "20", "MobileNetV2")

    st.markdown("<br>", unsafe_allow_html=True)

    # Feature cards
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div style="background: #0d1321; border: 1px solid rgba(0,255,136,0.15);
                    border-radius: 16px; padding: 1.8rem; height: 100%;
                    transition: all 0.3s;">
            <div style="font-size: 2.5rem; margin-bottom: 1rem;">📷</div>
            <div style="font-family: 'Syne', sans-serif; font-size: 1.1rem;
                        font-weight: 700; color: #00ff88; margin-bottom: 0.6rem;">
                Live Webcam
            </div>
            <div style="color: #6b7fa3; font-size: 0.9rem; line-height: 1.6;">
                Real-time detection from your camera with bounding boxes and
                confidence scores on every detected face.
            </div>
            <div style="margin-top: 1.2rem; font-size: 0.75rem; color: rgba(0,255,136,0.5);
                        text-transform: uppercase; letter-spacing: 0.1em; font-weight: 600;">
                → Live feed
            </div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div style="background: #0d1321; border: 1px solid rgba(0,255,136,0.15);
                    border-radius: 16px; padding: 1.8rem; height: 100%;">
            <div style="font-size: 2.5rem; margin-bottom: 1rem;">🖼️</div>
            <div style="font-family: 'Syne', sans-serif; font-size: 1.1rem;
                        font-weight: 700; color: #00ff88; margin-bottom: 0.6rem;">
                Image Upload
            </div>
            <div style="color: #6b7fa3; font-size: 0.9rem; line-height: 1.6;">
                Upload any photo and instantly analyse whether the detected
                face is wearing a mask or not.
            </div>
            <div style="margin-top: 1.2rem; font-size: 0.75rem; color: rgba(0,255,136,0.5);
                        text-transform: uppercase; letter-spacing: 0.1em; font-weight: 600;">
                → JPG / PNG
            </div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div style="background: #0d1321; border: 1px solid rgba(0,255,136,0.15);
                    border-radius: 16px; padding: 1.8rem; height: 100%;">
            <div style="font-size: 2.5rem; margin-bottom: 1rem;">📊</div>
            <div style="font-family: 'Syne', sans-serif; font-size: 1.1rem;
                        font-weight: 700; color: #00ff88; margin-bottom: 0.6rem;">
                Dashboard
            </div>
            <div style="color: #6b7fa3; font-size: 0.9rem; line-height: 1.6;">
                Explore training accuracy, loss curves, dataset distribution
                and full model architecture details.
            </div>
            <div style="margin-top: 1.2rem; font-size: 0.75rem; color: rgba(0,255,136,0.5);
                        text-transform: uppercase; letter-spacing: 0.1em; font-weight: 600;">
                → Stats & charts
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # How it works
    st.markdown("""
    <div style="font-family: 'Syne', sans-serif; font-size: 0.75rem; font-weight: 700;
                color: #6b7fa3; letter-spacing: 0.15em; text-transform: uppercase;
                margin-bottom: 1.2rem;">How it works</div>
    """, unsafe_allow_html=True)

    steps = st.columns(5)
    step_data = [
        ("01", "Input", "Camera or uploaded image"),
        ("02", "Detect", "Haar cascade finds faces"),
        ("03", "Crop", "Face region extracted"),
        ("04", "Predict", "MobileNetV2 classifies"),
        ("05", "Output", "Mask / No Mask + confidence"),
    ]
    for col, (num, title, desc) in zip(steps, step_data):
        with col:
            st.markdown(f"""
            <div style="background: #0d1321; border: 1px solid rgba(0,255,136,0.1);
                        border-radius: 12px; padding: 1.2rem; text-align: center;">
                <div style="font-family: 'Syne', sans-serif; font-size: 1.6rem;
                            font-weight: 800; color: rgba(0,255,136,0.2);
                            margin-bottom: 0.4rem;">{num}</div>
                <div style="font-family: 'Syne', sans-serif; font-size: 0.9rem;
                            font-weight: 700; color: #00ff88; margin-bottom: 0.3rem;">{title}</div>
                <div style="font-size: 0.75rem; color: #6b7fa3; line-height: 1.5;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

elif "📷" in page:
    import webcam_detection
    webcam_detection.show()

elif "🖼️" in page:
    import image_upload
    image_upload.show()

elif "📊" in page:
    import dashboard
    dashboard.show()