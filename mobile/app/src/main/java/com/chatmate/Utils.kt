package com.chatmate

import android.content.res.Resources

class Utils {

    /**
     * Converts pixels to density pixels
     * */
    private val scale: Float = Resources.getSystem().displayMetrics.density
    fun pxToDp(px: Int): Int {
        return (px * scale + 0.5f).toInt()
    }
}