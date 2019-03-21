import subprocess

class HdChecker():
    def launch_hd_space(self):
        """
        Method definition: use subprocess to call df -h output.
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

    def validate_output(self, output):
        """
        Method definition: use len of stdout and stderr to validate if output
        succeded or failed.
        """
        if len(output[0]) > 0:
            return True
        else:
            return False

    def parse_line(self, hd_space):
        """
        Method definition: parse line 3 from the df -h output
        """
        hd_space_list = hd_space[0].split('\n')
        return hd_space_list[3]

    def get_percentage(self,line_three):
        """
        Method definition: parse percentage from line 3 of output.
        """
        percentage = line_three.split()
        return percentage[4]

    def string_to_int(self, percentage):
        """
        Method definition: convert percentage string to int.
        """
        percentage_int = percentage[0:2]
        return int(percentage_int)

    def validate_percentage(self, percentage):
        """
        Method definition: return True if percentage is above 90%.
        """
        if percentage >= 90:
            return True
        else:
            return False


try:
    hd_check = HdChecker()
    hd_space = hd_check.launch_hd_space()
    valid_output = hd_check.validate_output(hd_space)
    if valid_output:
        line_three = hd_check.parse_line(hd_space)
        hd_percentage = hd_check.get_percentage(line_three)
        percentage_int = hd_check.string_to_int(hd_percentage)
        valid_percentage = hd_check.validate_percentage(percentage_int)
        if valid_percentage:
            print("WARNING, you're running low on HD space. "
                  "Currently at {}%".format(percentage_int))
        else:
            print('You currently have {}% HD space used.'
                  .format(percentage_int))
    else:
        print('ERROR:There was an issue runnning "df -h" on this system.')
except (KeyboardInterrupt, SystemExit):
        sys.exit(0)
