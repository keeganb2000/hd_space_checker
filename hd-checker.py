import subprocess

class HdChecker():
    def launch_hd_space(self):
        """
        Method definition:
        """
        hd_space = subprocess.Popen('df -h',
                                 shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE
                                 )
        stdout = hd_space.stdout.read()
        stderr = hd_space.stderr.read()
        hd_space.stdout.close()
        hd_space.stderr.close()
        return (stdout).decode('utf-8').strip('\n'), \
               (stderr).decode('utf-8').strip('\n')

    def parse_line(self, hd_space):
        """
        Method definition:
        """
        hd_space_list = hd_space[0].split('\n')
        return hd_space_list[3]

    def get_percentage(self,line_three):
        """
        Method definition:
        """
        percentage = line_three.split()
        return percentage[4]

    def string_to_int(self, percentage):
        percentage_int = percentage[0:2]
        return int(percentage_int)

    def validate_percentage(self, percentage):
        high = 34
        if high >= 0 and high <= 89:
            print('You have used up {}% of your HD Space and are within 0% <> 89% limits'.format(high))
        if high >= 90:
            print("WARNING, you're running low on HD space. Currently at {}%".format(high))



hd_check = HdChecker()
hd_space = hd_check.launch_hd_space()
line_three = hd_check.parse_line(hd_space)
hd_percentage = hd_check.get_percentage(line_three)
percentage_int = hd_check.string_to_int(hd_percentage)
valid_percentage = hd_check.validate_percentage(percentage_int)
