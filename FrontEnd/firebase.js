// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBGXz1N9v7RsOf8YD4vBWfBZIKd_ZUR8m0",
  authDomain: "appz-c6cda.firebaseapp.com",
  projectId: "appz-c6cda",
  storageBucket: "appz-c6cda.firebasestorage.app",
  messagingSenderId: "159379526695",
  appId: "1:159379526695:web:1fb8ec9f9e812ab6526a02",
  measurementId: "G-6709DGNBVZ"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);