[app]
title = My Application
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[android]
android.sdk = 33
android.build_tools = 33.0.0
android.api = 34
android.minapi = 21
android.ndk = 25b
android.ndk_path = $HOME/.buildozer/android/platform/android-ndk-r25b
android.sdk_path = $HOME/.buildozer/android/platform/android-sdk/tools/bin/sdkmanager
android.gradle_dependencies = com.android.tools.build:gradle:7.3.3
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.debug_artifact = apk
android.release_artifact = aab








