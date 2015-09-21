from __future__ import absolute_import, print_function

import yaml

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Compiles the regex patterns that ua_agent needs from their yaml fixture'

    def handle(self, **options):
        with open('src/sentry/utils/ua_parser/regexes.yaml') as fp:
            regexes = yaml.safe_load(fp)

        with open('src/sentry/utils/ua_parser/_regexes.py', 'wb') as fp:
            fp.write('###########################################\n')
            fp.write('# NOTICE: This file is autogenerated from #\n')
            fp.write('# regexes.yaml. Do not edit by hand,      #\n')
            fp.write('# instead, re-run `sentry compileregexes` #\n')
            fp.write('###########################################\n')
            fp.write('from __future__ import absolute_import\n')
            fp.write('\n')
            fp.write('from .parser import (\n')
            fp.write('    UserAgentParser, DeviceParser, OSParser,\n')
            fp.write(')\n')
            fp.write('\n\n')
            fp.write('USER_AGENT_PARSERS = [\n')
            for device_parser in regexes['user_agent_parsers']:
                fp.write('    UserAgentParser(\n')
                fp.write('        %r,\n' % device_parser['regex'])
                fp.write('        %r,\n' % device_parser.get('family_replacement'))
                fp.write('        %r,\n' % device_parser.get('v1_replacement'))
                fp.write('        %r,\n' % device_parser.get('v2_replacement'))
                fp.write('    ),\n')
            fp.write(']\n')
            fp.write('\n')
            fp.write('DEVICE_PARSERS = [\n')
            for device_parser in regexes['device_parsers']:
                fp.write('    DeviceParser(\n')
                fp.write('        %r,\n' % device_parser['regex'])
                fp.write('        %r,\n' % device_parser.get('regex_flag'))
                fp.write('        %r,\n' % device_parser.get('device_replacement'))
                fp.write('        %r,\n' % device_parser.get('brand_replacement'))
                fp.write('        %r,\n' % device_parser.get('model_replacement'))
                fp.write('    ),\n')
            fp.write(']\n')
            fp.write('\n')
            fp.write('OS_PARSERS = [\n')
            for device_parser in regexes['os_parsers']:
                fp.write('    OSParser(\n')
                fp.write('        %r,\n' % device_parser['regex'])
                fp.write('        %r,\n' % device_parser.get('os_replacement'))
                fp.write('        %r,\n' % device_parser.get('os_v1_replacement'))
                fp.write('        %r,\n' % device_parser.get('os_v2_replacement'))
                fp.write('    ),\n')
            fp.write(']\n')
