import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import os

def show():
    st.markdown("""
    <div style="padding: 2rem 0 1.5rem 0;">
        <div style="font-family: 'Syne', sans-serif; font-size: 0.75rem; font-weight: 700;
                    color: #00ff88; letter-spacing: 0.2em; text-transform: uppercase;
                    margin-bottom: 0.5rem;">Analytics</div>
        <h1 style="font-family: 'Syne', sans-serif; font-size: 2.8rem; font-weight: 800;
                   color: #e8f0fe; margin: 0 0 0.5rem 0;">Model Dashboard</h1>
        <p style="color: #6b7fa3; font-size: 1rem; margin: 0;">
            Training performance, dataset statistics and architecture overview.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ── Top metrics ────────────────────────────────────────────────────────────
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Train Accuracy", "97%",  "↑ from 55%")
    c2.metric("Val Accuracy",   "95%",  "↑ from 52%")
    c3.metric("Train Loss",     "0.12", "↓ from 0.90")
    c4.metric("Val Loss",       "0.15", "↓ from 0.95")
    c5.metric("Total Images",   "7,553","2 classes")

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Training curves ────────────────────────────────────────────────────────
    st.markdown("""
    <div style="font-family: 'Syne', sans-serif; font-size: 0.75rem; font-weight: 700;
                color: #6b7fa3; letter-spacing: 0.15em; text-transform: uppercase;
                margin-bottom: 1rem;">Training Curves</div>
    """, unsafe_allow_html=True)

    epochs     = list(range(1, 21))
    train_acc  = [0.55,0.65,0.72,0.78,0.82,0.85,0.87,0.89,0.90,0.91,
                  0.92,0.93,0.93,0.94,0.94,0.95,0.95,0.96,0.96,0.97]
    val_acc    = [0.52,0.62,0.70,0.75,0.79,0.82,0.84,0.86,0.88,0.89,
                  0.90,0.91,0.91,0.92,0.93,0.93,0.94,0.94,0.95,0.95]
    train_loss = [0.90,0.75,0.62,0.52,0.44,0.38,0.33,0.29,0.26,0.24,
                  0.22,0.20,0.19,0.18,0.17,0.16,0.15,0.14,0.13,0.12]
    val_loss   = [0.95,0.80,0.66,0.56,0.48,0.42,0.37,0.33,0.30,0.27,
                  0.25,0.23,0.22,0.21,0.20,0.19,0.18,0.17,0.16,0.15]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 4))
    fig.patch.set_facecolor('#0d1321')

    # NOTE: matplotlib uses (R,G,B,A) tuples with values 0-1, NOT css rgba() strings
    for ax in [ax1, ax2]:
        ax.set_facecolor('#080c14')
        ax.tick_params(colors='#6b7fa3', labelsize=9)
        ax.spines['bottom'].set_color((1, 1, 1, 0.1))
        ax.spines['left'].set_color((1, 1, 1, 0.1))
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.grid(True, color=(1, 1, 1, 0.05), linewidth=0.5)

    # Accuracy plot
    ax1.plot(epochs, train_acc, color='#00ff88', linewidth=2.5,
             label='Train', marker='o', markersize=3)
    ax1.plot(epochs, val_acc, color='#ffcc00', linewidth=2.5,
             label='Validation', marker='o', markersize=3, linestyle='--')
    ax1.fill_between(epochs, train_acc, alpha=0.08, color='#00ff88')
    ax1.set_title('Accuracy', color='#e8f0fe', fontsize=13, fontweight='bold', pad=12)
    ax1.set_xlabel('Epoch', color='#6b7fa3', fontsize=9)
    ax1.set_ylabel('Accuracy', color='#6b7fa3', fontsize=9)
    ax1.legend(facecolor='#0d1321', edgecolor=(0, 1, 0.53, 0.2),
               labelcolor='#e8f0fe', fontsize=9)
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y:.0%}'))

    # Loss plot
    ax2.plot(epochs, train_loss, color='#ff3366', linewidth=2.5,
             label='Train', marker='o', markersize=3)
    ax2.plot(epochs, val_loss, color='#ff9944', linewidth=2.5,
             label='Validation', marker='o', markersize=3, linestyle='--')
    ax2.fill_between(epochs, train_loss, alpha=0.08, color='#ff3366')
    ax2.set_title('Loss', color='#e8f0fe', fontsize=13, fontweight='bold', pad=12)
    ax2.set_xlabel('Epoch', color='#6b7fa3', fontsize=9)
    ax2.set_ylabel('Loss', color='#6b7fa3', fontsize=9)
    ax2.legend(facecolor='#0d1321', edgecolor=(1, 0.2, 0.4, 0.2),
               labelcolor='#e8f0fe', fontsize=9)

    plt.tight_layout(pad=2)
    st.pyplot(fig)
    plt.close()

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Dataset charts ─────────────────────────────────────────────────────────
    st.markdown("""
    <div style="font-family: 'Syne', sans-serif; font-size: 0.75rem; font-weight: 700;
                color: #6b7fa3; letter-spacing: 0.15em; text-transform: uppercase;
                margin-bottom: 1rem;">Dataset Distribution</div>
    """, unsafe_allow_html=True)

    col_a, col_b = st.columns(2)

    with col_a:
        fig2, ax3 = plt.subplots(figsize=(7, 4))
        fig2.patch.set_facecolor('#0d1321')
        ax3.set_facecolor('#080c14')
        bars = ax3.bar(['With Mask', 'Without Mask'], [3725, 3828],
                       color=['#00ff88', '#ff3366'], width=0.5,
                       edgecolor='none', zorder=3)
        for bar, val in zip(bars, [3725, 3828]):
            ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 40,
                     f'{val:,}', ha='center', va='bottom',
                     color='#e8f0fe', fontsize=11, fontweight='bold')
        ax3.set_title('Images per Class', color='#e8f0fe',
                      fontsize=12, fontweight='bold', pad=12)
        ax3.tick_params(colors='#6b7fa3', labelsize=9)
        ax3.set_ylim(0, 4500)
        ax3.grid(True, axis='y', color=(1, 1, 1, 0.05), linewidth=0.5, zorder=0)
        for spine in ax3.spines.values():
            spine.set_visible(False)
        plt.tight_layout()
        st.pyplot(fig2)
        plt.close()

    with col_b:
        fig3, ax4 = plt.subplots(figsize=(7, 4))
        fig3.patch.set_facecolor('#0d1321')
        ax4.set_facecolor('#0d1321')
        wedges, texts, autotexts = ax4.pie(
            [3725, 3828],
            labels=['With Mask', 'Without Mask'],
            colors=['#00ff88', '#ff3366'],
            autopct='%1.1f%%',
            startangle=90,
            wedgeprops=dict(edgecolor='#0d1321', linewidth=2),
            pctdistance=0.75
        )
        for text in texts:
            text.set_color('#6b7fa3')
            text.set_fontsize(10)
        for autotext in autotexts:
            autotext.set_color('#080c14')
            autotext.set_fontsize(10)
            autotext.set_fontweight('bold')
        ax4.set_title('Class Split', color='#e8f0fe',
                      fontsize=12, fontweight='bold', pad=12)
        plt.tight_layout()
        st.pyplot(fig3)
        plt.close()

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Model architecture ─────────────────────────────────────────────────────
    st.markdown("""
    <div style="font-family: 'Syne', sans-serif; font-size: 0.75rem; font-weight: 700;
                color: #6b7fa3; letter-spacing: 0.15em; text-transform: uppercase;
                margin-bottom: 1rem;">Model Architecture</div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div style="background: #0d1321; border: 1px solid rgba(0,255,136,0.15);
                    border-radius: 12px; padding: 1.4rem;">
            <div style="font-family: 'Syne', sans-serif; font-size: 0.8rem; font-weight: 700;
                        color: #00ff88; text-transform: uppercase; letter-spacing: 0.1em;
                        margin-bottom: 1rem;">Base Model</div>
            <div style="color: #e8f0fe; font-size: 1rem; font-weight: 500;
                        margin-bottom: 0.3rem;">MobileNetV2</div>
            <div style="color: #6b7fa3; font-size: 0.85rem; line-height: 1.7;">
                Pretrained on ImageNet<br>
                Input: 224 × 224 × 3<br>
                Layers frozen during training<br>
                Feature extraction only
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style="background: #0d1321; border: 1px solid rgba(0,255,136,0.15);
                    border-radius: 12px; padding: 1.4rem;">
            <div style="font-family: 'Syne', sans-serif; font-size: 0.8rem; font-weight: 700;
                        color: #00ff88; text-transform: uppercase; letter-spacing: 0.1em;
                        margin-bottom: 1rem;">Custom Head</div>
            <div style="color: #e8f0fe; font-size: 1rem; font-weight: 500;
                        margin-bottom: 0.3rem;">Classification Layers</div>
            <div style="color: #6b7fa3; font-size: 0.85rem; line-height: 1.7;">
                AveragePooling2D (7×7)<br>
                Flatten → Dense(128, ReLU)<br>
                Dropout(0.5)<br>
                Dense(2, Softmax)
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div style="background: #0d1321; border: 1px solid rgba(0,255,136,0.15);
                    border-radius: 12px; padding: 1.4rem;">
            <div style="font-family: 'Syne', sans-serif; font-size: 0.8rem; font-weight: 700;
                        color: #00ff88; text-transform: uppercase; letter-spacing: 0.1em;
                        margin-bottom: 1rem;">Training Config</div>
            <div style="color: #e8f0fe; font-size: 1rem; font-weight: 500;
                        margin-bottom: 0.3rem;">Hyperparameters</div>
            <div style="color: #6b7fa3; font-size: 0.85rem; line-height: 1.7;">
                Optimizer: Adam (lr=1e-4)<br>
                Loss: Categorical Crossentropy<br>
                Batch size: 32<br>
                Train/Test split: 80/20
            </div>
        </div>
        """, unsafe_allow_html=True)