package com.chatmate

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.EditText
import android.widget.TextView

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val utils = Utils()

        fun setErrorMsg(field: TextView, msg: String) {
            field.height = utils.pxToDp(20)
            field.text = msg
        }

        val btnSignUp: TextView = findViewById(R.id.no_account)
        btnSignUp.setOnClickListener {
            val intent = Intent(this@MainActivity, RegisterActivity::class.java)
            startActivity(intent)
        }

        val btnLogin: TextView = findViewById(R.id.btn_login)
        btnLogin.setOnClickListener {
            // Username
            val inputUsername: EditText = findViewById(R.id.inputUsernameLogin)
            val username = inputUsername.text
            // Password
            val inputPassword: EditText = findViewById(R.id.inputPasswordLogin)
            val password = inputPassword.text

            println("username $username & passwd $password")

            val txtFeedback: TextView = findViewById(R.id.textFeedback)
            txtFeedback.text = ""

            // Login
            setErrorMsg(txtFeedback, "Login not implemented yet.")
        }
    }
}