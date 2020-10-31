import subprocess
import os


class Runner(object):

    def __init__(self, code, lang, username, output, input_str, type_input, type_run):
        self.code = code
        self.lang = lang
        self.username = username
        self.CURRENT_LANG = ['Python', 'C++', 'PASCAL']
        self.CURRENT_TYPE_INPUT = ['FILE', 'STRING']
        self.CURRENT_TYPE_RUN = ['TEST','ONLINE']
        self.CURRENT_PATH = os.getcwd()
        self.output = output
        self.input_str = input_str
        self.type_input = type_input
        self.type_run = type_run

    def create_main_file(self, file_name):
        file = open(file_name, 'w')
        file.write(self.code)
        file.close()
        return True

    def create_file(self, i):
        file = open('input.bat', 'w')
        file.write(self.input_str[i])
        file.close()
        return True

    def check_result(self, i, result, result_func):
        if result.stdout.strip() == self.output[i]:
            result_func['tests'].append('OK')
        else:
            result_func['tests'].append('ERROR')
        return True

    def run_compile(self):
        if self.lang == self.CURRENT_LANG[0]:
            return self.run_python()
        elif self.lang == self.CURRENT_LANG[1]:
            return self.run_cplusplus()
        elif self.lang == self.CURRENT_LANG[2]:
            return self.run_pascal()

    def run_cplusplus(self):
        result_func = {'status': None, 'tests': []}
        file_name = self.username + r'.cpp'
        file_name_exe = self.username + r'.exe'
        self.create_main_file(file_name)
        compile_file = subprocess.run(['g++', file_name, '-o', file_name_exe],
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
        if compile_file.returncode == 0:
            result_func['status'] = 'OK'
            for i in range(len(self.input_str)):
                if self.type_input == self.CURRENT_TYPE_INPUT[0]:
                    self.create_file(i)
                    result = subprocess.run([file_name_exe],
                                            stdout=subprocess.PIPE,
                                            text=True,
                                            stderr=subprocess.PIPE)
                    os.remove('input.bat')
                elif self.type_input == self.CURRENT_TYPE_INPUT[1]:
                    result = subprocess.run([file_name_exe],
                                            stdout=subprocess.PIPE,
                                            text=True,
                                            stderr=subprocess.PIPE,
                                            input=self.input_str[i])
                if result.returncode == 0:
                    if self.CURRENT_TYPE_RUN[0] == self.type_run:
                        self.check_result(i, result, result_func)
                    elif self.CURRENT_TYPE_RUN[1] == self.type_run:
                        result_func.appent(result.stdout.strip())
                else:
                    result_func['status'] = 'ERROR'
                    result_func['tests'].append(result.stderr.strip())
                    break
            os.remove(file_name_exe)
        else:
            result_func['status'] = 'ERROR'
            result_func['tests'].append(compile_file.stderr.strip())
        os.remove(file_name)
        return result_func

    def run_python(self):
        result_func = {'status': None, 'tests': []}
        file_name = self.username + r'.py'
        self.create_main_file(file_name)
        for i in range(len(self.input_str)):
            if self.type_input == self.CURRENT_TYPE_INPUT[0]:
                self.create_file(i)
                result = subprocess.run(['python', file_name],
                                        stdout=subprocess.PIPE,
                                        text=True,
                                        stderr=subprocess.PIPE)
                os.remove('input.bat')
            elif self.type_input == self.CURRENT_TYPE_INPUT[1]:
                result = subprocess.run(['python', file_name],
                                        stdout=subprocess.PIPE,
                                        text=True,
                                        stderr=subprocess.PIPE,
                                        input=self.input_str[i])
            if result.returncode == 0:
                result_func['status'] = 'OK'
                if self.CURRENT_TYPE_RUN[0] == self.type_run:
                    self.check_result(i, result, result_func)
                elif self.CURRENT_TYPE_RUN[1] == self.type_run:
                    result_func.appent(result.stdout.strip())
            else:
                result_func['status'] = "ERROR"
                result_func['tests'].append(result.stderr)
                break
        os.remove(file_name)
        return result_func

    def run_pascal(self):
        result_func = {'status': None, 'tests': []}
        file_name = self.username + r'.pas'
        file_name_exe = self.username + r'.exe'
        self.create_main_file(file_name)
        compile_file = subprocess.run([r'C:\FPC\3.2.0\bin\i386-win32\ppc386.exe', file_name],
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
        if compile_file.returncode == 0:
            result_func['status'] = 'OK'
            for i in range(len(self.input_str)):
                if self.type_input == self.CURRENT_TYPE_INPUT[0]:
                    self.create_file(i)
                    result = subprocess.run([file_name_exe],
                                            stdout=subprocess.PIPE,
                                            text=True,
                                            stderr=subprocess.PIPE)
                    os.remove('input.bat')
                elif self.type_input == self.CURRENT_TYPE_INPUT[1]:
                    result = subprocess.run([file_name_exe],
                                            stdout=subprocess.PIPE,
                                            text=True,
                                            stderr=subprocess.PIPE,
                                            input=self.input_str[i])
                if result.returncode == 0:
                    if self.CURRENT_TYPE_RUN[0] == self.type_run:
                        self.check_result(i, result, result_func)
                    elif self.CURRENT_TYPE_RUN[1] == self.type_run:
                        result_func.appent(result.stdout.strip())
                else:
                    result_func['status'] = 'ERROR'
                    result_func['tests'].append(result.stderr.strip())
                    break
            os.remove(file_name_exe)
            os.remove(self.username+r'.o')
        else:
            result_func['status'] = 'ERROR'
            result_func['tests'].append(compile_file.stdout.strip())
        os.remove(file_name)
        return result_func
