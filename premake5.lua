workspace "wvatha"
    startproject "wvatha_editor"
    architecture "x64"
    location "build"

    configurations {
        "Debug",
        "Release"
    }

project "wvatha_editor"
    location "wvatha_editor"
    kind "ConsoleApp"
    language "C++"
    cppdialect "C++17"

    files {
        "%{prj.name}/src/**.h",
        "%{prj.name}/src/**.cpp"
    }

    flags {
        "FatalWarnings"
    }