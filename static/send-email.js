const generateOTP = () => {
  let OTP = Math.round(Math.random() * 10 * new Date().getMilliseconds());
  return OTP;
};

let otp = generateOTP();

const Cryptography_Encrypt = (text) => {
  let encryptedStr = "";

  const url = `https://ampplex-backened.herokuapp.com/EncryptData/${text}`;

  fetch(url, {
    method: "GET",
    headers: { "Content-Type": "application/json" },
    mode: "no-cors",
  })
    .then((res) => res.json())
    .then((data) => {
      encryptedStr = data.encrypted_text;
    });

  return encryptedStr;
};

const sendOTP = () => {
  let templateParams = {
    message: `Your OTP is ${otp}. Please do not share it with anyone`,
    to_email: document.getElementById("email").value, // Enter your email address
  };

  emailjs.send("service_3r9q6dj", "template_6lrma6o", templateParams).then(
    function (response) {
      location.href = `/EnterOTP/${Cryptography_Encrypt(otp.toString())}/${
        document.getElementById("email").value
      }`;
    },
    function (error) {}
  );
};

document.getElementById("verify_email").addEventListener("click", () => {
  if (document.getElementById("email").value.length >= 3) {
    sendOTP(); // Uncomment this line to send OTP to your email
  }
});
