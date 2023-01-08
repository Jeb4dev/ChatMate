package com.chatmate

import android.os.Bundle
import android.widget.EditText
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity


class RegisterActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_register)

        val utils = Utils()
        var formValid: Boolean


        fun setErrorMsg(field: TextView, msg: String) {
            field.height = utils.pxToDp(20)
            field.text = msg
            formValid = false
        }

        val txtView: TextView = findViewById(R.id.already_account)
        txtView.setOnClickListener {
            // Finish activity (back to previous activity)
            finish()
        }


        val btnRegister: TextView = findViewById(R.id.btn_register)
        btnRegister.setOnClickListener {
            formValid = true
            // Username
            val inputUsername: EditText = findViewById(R.id.inputUsername)
            val username = inputUsername.text
            // Password
            val inputPassword: EditText = findViewById(R.id.inputPassword)
            val password = inputPassword.text
            // Password Confirmation
            val inputPassword2: EditText = findViewById(R.id.inputPassword2)
            val password2 = inputPassword2.text

            println("username $username & passwd $password & passwd2 $password2")


            val txtFeedbackUsername: TextView = findViewById(R.id.textRegisterUsernameFeedback)
            val txtFeedbackPassword: TextView = findViewById(R.id.textRegisterPasswordFeedback)

            // Reset feedback
            txtFeedbackUsername.text = ""
            txtFeedbackPassword.text = ""

            // Validate Username
            if (username.length < 3) {
                setErrorMsg(txtFeedbackUsername, "Username must be at least 3 characters")
            }

            // Validate Password
            if (password.length >= 8) { // greater than or equal to 7
                if (password.length <= 64) { // less than or equal to 64
                    if (password.toString() != password2.toString()) { // equals
                        setErrorMsg(txtFeedbackPassword, "Passwords doesn't match")
                    }
                } else {
                    setErrorMsg(txtFeedbackPassword, "Password must be at most 64 characters")
                }
            } else {
                setErrorMsg(txtFeedbackPassword, "Password must be at least 8 characters")
            }

            // Form was valid
            if (formValid) {
                setErrorMsg(txtFeedbackUsername, "Registration not yet fully implemented.")
            }

        }
    }
}