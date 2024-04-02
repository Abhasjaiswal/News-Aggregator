import streamlit as st

def display_contact():
# CSS styling
    st.markdown("""
    <style>
    /* Google Font CDN Link */
    @import url("https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap");
    * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Poppins", sans-serif;
    }
    body {
    min-height: 100vh;
    width: 100%;
    background: #1e1e1e;
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    }
    .container {
    max-width: 1100px;
    width: 100%;
    background: #2b2b2b;
    border-radius: 6px;
    padding: 20px 60px 30px 40px;
    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
    }
    .container .content {
    display: flex;
    align-items: center;
    justify-content: space-between;
    }
    .container .content .left-side {
    width: 25%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-top: 15px;
    position: relative;
    }
    .content .left-side::before {
    content: "";
    position: absolute;
    height: 70%;
    width: 2px;
    right: -15px;
    top: 50%;
    transform: translateY(-50%);
    background: #555;
    }
    .content .left-side .details {
    margin: 14px;
    text-align: center;
    }
    .content .left-side .details i {
    font-size: 30px;
    color: #fff; /* Changed icon color to white */
    margin-bottom: 10px;
    }
    .content .left-side .details .topic {
    font-size: 18px;
    font-weight: 500;
    }
    .content .left-side .details .text-one,
    .content .left-side .details .text-two {
    font-size: 14px;
    color: #afafb6;
    }

    .container .content .right-side {
    width: 75%;
    margin-left: 75px;
    }
    .content .right-side .topic-text {
    font-size: 23px;
    font-weight: 600;
    color: #fff; /* Changed blue text to white */
    }
    .right-side .input-box {
    height: 55px;
    width: 100%;
    margin: 12px 0;
    }
    .right-side .input-box input,
    .right-side .input-box textarea {
    height: 100%;
    width: 100%;
    border: none;
    outline: none;
    font-size: 16px;
    background: #444;
    border-radius: 6px;
    padding: 0 15px;
    color: #fff;
    }
    .right-side .message-box {
    min-height: 110px;
    }
    .right-side .input-box textarea {
    padding-top: 6px;
    }
    .right-side .button {
    display: inline-block;
    margin-top: 12px;
    }
    .right-side .button input[type="button"] {
    color: #fff;
    font-size: 18px;
    outline: none;
    border: none;
    padding: 8px 16px;
    border-radius: 6px;
    background: #3e2093;
    cursor: pointer;
    transition: all 0.3s ease;
    }
    .button input[type="button"]:hover {
    background: #5029bc;
    }

    @media (max-width: 950px) {
    .container {
        width: 90%;
        padding: 30px 40px 40px 35px;
    }
    .container .content .right-side {
        width: 75%;
        margin-left: 55px;
    }
    }
    @media (max-width: 820px) {
    .container {
        margin: 40px 0;
        height: 100%;
    }
    .container .content {
        flex-direction: column-reverse;
    }
    .container .content .left-side {
        width: 100%;
        flex-direction: row;
        margin-top: 40px;
        justify-content: center;
        flex-wrap: wrap;
    }
    .container .content .left-side::before {
        display: none;
    }
    .container .content .right-side {
        width: 100%;
        margin-left: 0;
    }
    }
    </style>
    """, unsafe_allow_html=True)

    # HTML structure
    st.markdown("""
    <!DOCTYPE html>
    <!-- Website - www.codingnepalweb.com -->
    <html lang="en" dir="ltr">
    <head>
        <meta charset="UTF-8" />
        <title>Responsive Contact Us Form | CodingLab</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.2/css/all.min.css" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    </head>
    <body>
        <div class="container">
        <div class="content">
            <div class="left-side">
            <div class="address details">
                <i class="fas fa-map-marker-alt"></i>
                <div class="topic">Address</div>
                <div class="text-one">School of Computer Science</div>
                <div class="text-two">UPES,Dehradun</div>
            </div>
            <div class="phone details">
                <i class="fas fa-phone-alt"></i>
                <div class="topic">Phone</div>
                <div class="text-one">+91 8948215149</div>
            </div>
            <div class="email details">
                <i class="fas fa-envelope"></i>
                <div class="topic">Email</div>
                <div class="text-one">abhas.jaiswal0907@gmail.com</div>
                <div class="text-two">abhas.122850@stu.upes.ac.in</div>
            </div>
            </div>
            <div class="right-side">
            <div class="topic-text">Send us a message</div>
            <p>If you have any work from me or any types of queries related to my project, you can send me a message from here. It's my pleasure to help you.</p>
            <form action="#">
                <div class="input-box">
                <input type="text" placeholder="Enter your name" />
                </div>
                <div class="input-box">
                <input type="text" placeholder="Enter your email" />
                </div>
                <div class="input-box message-box">
                <textarea placeholder="Enter your message"></textarea>
                </div>
                <div class="button">
                <input type="button" value="Send Now" />
                </div>
            </form>
            </div>
        </div>
        </div>
    </body>
    </html>
    """, unsafe_allow_html=True)

