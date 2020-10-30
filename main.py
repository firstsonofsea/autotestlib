import subprocess
import os


class Runner(object):

    def __init__(self, file, lang, username, output, input_str):
        self.file = file
        self.lang = lang
        self.username = username
        self.CURRENT_LANG = ['Python', 'C++']
        self.CURRENT_PATH = os.getcwd()
        self.output = output
        self.input_str = input_str

    def run_compile(self):
        if self.lang == self.CURRENT_LANG[0]:
            return self.run_python()
        elif self.lang == self.CURRENT_LANG[1]:
            return self.run_cplusplus()

    def run_cplusplus(self):
        result_func = {'status': None, 'tests': []}
        file_name = self.username + r'.cpp'
        file_name_exe = self.username + r'.exe'
        file = open(file_name, 'w')
        file.write(self.file)
        file.close()
        compile_file = subprocess.run(['g++', file_name, '-o', file_name_exe],
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
        if compile_file.returncode == 0:
            result_func['status'] = 'OK'
            for i in range(len(self.input_str)):
                result = subprocess.run([file_name_exe],
                                        stdout=subprocess.PIPE,
                                        text=True,
                                        stderr=subprocess.PIPE,
                                        input=self.input_str[i])
                if result.returncode == 0:
                    if result.stdout.strip()[:-44] == self.output[i]:
                        result_func['tests'].append('OK')
                    else:

                        result_func['tests'].append('ERROR')
                else:
                    result_func['status'] = 'ERROR'
                    result_func['tests'].append(result.stderr.strip())
                    break
        else:
            result_func['status'] = 'ERROR'
            result_func['tests'].append(compile_file.stderr.strip())
        os.remove(file_name)
        if os.path.exists(file_name_exe):
            os.remove(file_name_exe)
        return result_func

    def run_python(self):
        result_func = {'status': None, 'tests': []}
        file_name = self.username + r'.py'
        file = open(file_name, 'w')
        file.write(self.file)
        file.close()
        for i in range(len(self.input_str)):
            result = subprocess.run(['python', file_name],
                                    stdout=subprocess.PIPE,
                                    text=True,
                                    stderr=subprocess.PIPE,
                                    input=self.input_str[i])
            if result.returncode == 0:
                result_func['status'] = 'OK'
                if result.stdout.strip() == self.output[i]:
                    result_func['tests'].append('OK')
                else:
                    result_func['tests'].append('ERROR')
            else:
                result_func['status'] = "ERROR"
                result_func['tests'].append(result.stderr)
                break
        os.remove(file_name)
        return result_func
