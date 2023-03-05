import React from 'react'
import './Landing.css'
function Landing() {
    return (
        <div>
            <div className="header">
                <img id="img1" src="Chakra.svg" />
                <p id="lip"> <span>Lorem</span>ipsum</p>
            </div>
            <div className="welcome">
                <p id="wtxt1">Welcome to the new way of quizzes</p>
                <p id="wtxt2">We are a platform dedicated to quizzes, where you can create, share, and participate in various quizzes on a wide range of topics.</p>
                <button className="button"><span>Take me there</span></button>
            </div>
        </div>
    )
}

export default Landing