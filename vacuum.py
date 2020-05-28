from pathlib import Path
from collections import namedtuple
import json

# traits

class Show:
    def __repr__(self):
        return str(self.__dict__)

# core

class Package(Show):
    def __init__(self, path, manifest):
        self.path = path
        self.manifest = manifest
        
class Manifest(Show):
    def __init__(self, name, version, targets):
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
    def __init__(self, name, build_directory, source_files, include_directories, standart):
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

NewOptions = namedtuple('NewOptions', 'name path kind')

def new(options):
    (options.path / options.name).mkdir()
    (options.path / options.name / 'src').mkdir()
    (options.path / options.name / 'include').mkdir()
    (options.path / options.name / 'include' / options.name).mkdir()
    
    with (options.path / options.name / 'vacuum.json').open('w') as file:
        json.dump({
            'name': options.name,
            'version': '0.1',
            'targets': [
                {
                    'name': options.name,
                    'kind': options.kind,
                    'source_files': ['src/main.cpp'] if options.kind == 'executable' else [],
                    'include_directories': ['include'],
                    'standart': '17',
                    'build_directory': f'build/{options.name}'
                }
            ]
        }, file, indent=4)
        
    if options.kind == 'executable':
        with (options.path / options.name / 'src' / 'main.cpp').open('w') as file:
            file.write('#include <iostream>\n')
            file.write('\n')
            file.write('int main() {\n')
            file.write('\tstd::cout << "Hello World!\\n";\n')
            file.write('\treturn 0;\n')
            file.write('}')

# main