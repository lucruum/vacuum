# traits

class Show:
    def __repr__(self):
        return str(self.__dict__)

# core

class Package(Show):
    def __init__(self, *, path, manifest):
        self.path = path
        self.manifest = manifest
        
class Manifest(Show):
    def __init__(self, *, name, version, targets):
        self.name = name
        self.version = version
        self.targets = targets
        
class Target(Show):
    def build(self):
        raise NotImplementedError()
        
    def run(self):
        raise NotImplementedError()
        
    def clean(self):
        raise NotImplementedError()
        
class CompilerTarget(Target):
    def __init__(self, *, name, build_directory, source_files, include_directories, standart):
        self.name = name
        self.build_directory = build_directory
        self.source_files = source_files
        self.include_directories = include_directories
        self.standart = standart
        
class LibraryTarget(CompilerTarget):
    pass
    
class ExecutableTarget(CompilerTarget):
    pass
    
# commands

# main
