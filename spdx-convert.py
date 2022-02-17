# SPDX-License-Identifier: Apache-2.0

def insert_license():

    import os

    # Create an array of paths mirroring structure of current directory
    # while ignoring this script and problematic file types
    for root, dirs, files in os.walk('.', topdown=False):
        paths = []
        for f in files:
            if f == 'spdx-convert.py':
                continue
            elif '.data' in f:
                continue
            elif '.png' in f:
                continue
            elif '.jar' in f:
                continue
            elif '.' not in f:
                continue
            elif '.pack' in f:
                continue
            elif '.idx' in f:
                continue
            else:
                path = os.path.join(root, f)
                paths.append(path)

        # Iterate through file paths, replacing block license text if found or 
        # identifying file type and adding appropriate license text to file
        for p in paths:        
            with open(p, 'r') as t:
                str_contents = t.read()
                if 'Licensed under' in str_contents:
                    beg = str_contents.find('Licensed under')
                    end = str_contents.find('limitations under the License.') + 29
                    str_contents = str_contents[0:beg] + 'SPDX-License-Identifier: Apache-2.0' + str_contents[end:-1] + '\n'
                    with open(p, 'w') as t:
                        t.write(str_contents)
                else:
                    with open(p, 'r') as t:
                        contents = t.readlines()
                        if p[-4:] == 'java':
                            contents.insert(0, '/* SPDX-License-Identifier: Apache-2.0 */\n\n')
                        elif p[-2:] == 'py' or p[-2:] == 'sh':
                            contents.insert(0, '# SPDX-License-Identifier: Apache-2.0\n\n')
                        elif p[-2:] == 'md':
                            contents.insert(0, '<!-- SPDX-License-Identifier: Apache-2.0 -->\n\n')
                        elif p[-3:] == 'txt':
                            contents.insert(0, 'SPDX-License-Identifier: Apache-2.0\n\n')
                    with open(p, 'w') as t:
                        contents = ''.join(contents)
                        t.write(contents)

insert_license()