import os
import subprocess

from conans import ConanFile, CMake, tools

class SDSLLite(ConanFile):
    name = "sdsl-lite"
    libname = "sdsl"
    exports_sources = "CMakeLists.txt"
    generators = "cmake"
    settings = "os", "compiler", "build_type", "arch"
    _source_subfolder = "sdsl-lite"
    _build_subfolder = "build_folder"
    version = "2.1.1"
    git_url = "https://github.com/simongog/sdsl-lite.git"

    def source(self):
        extracted_dir = "sdsl-lite-%s" % self.version
        os.system('git clone %s --branch "v%s" %s' % (self.git_url, self.version, extracted_dir))
        os.rename(extracted_dir, self._source_subfolder)

    def build(self):
        c = CMake(self)
        c.configure()
        c.build()

    def package(self):
        self.copy("*.h",   dst="include/", src="sdsl-lite/include")
        self.copy("*.hpp", dst="include/", src="sdsl-lite/include")
        self.copy("*.a",   dst="lib", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="lib", keep_path=False)
        self.copy("*.pdb", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs.append(self.libname)