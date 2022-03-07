import sys
import requests
import json

example_input_option = "mac"
ec2_meta_core = "http://169.254.169.254/latest/meta-data/"

## With more time, i'd expand this to match all possible end-points
## but for the sake of time only supporting immediate parent paths.

# Supported options

# ami-id
# ami-launch-index
# ami-manifest-path
# hostname
# instance-action
# instance-id
# instance-life-cycle
# instance-type
# local-hostname
# local-ipv4
# mac
# profile
# public-hostname
# public-ipv4
# reservation-id
# security-groups

## Unsupported options

# block-device-mapping/
# events/
# hibernation/
# identity-credentials/
# managed-ssh-keys/
# metrics/
# network/
# placement/
# public-keys/

if __name__ == "__main__":

    list_supported = [
        'ami-id',
        'ami-launch-index',
        'ami-manifest-path',
        'hostname',
        'instance-action',
        'instance-id',
        'instance-life-cycle',
        'instance-type',
        'local-hostname',
        'local-ipv4',
        'mac',
        'profile',
        'public-hostname',
        'public-ipv4',
        'reservation-id',
        'security-groups'
    ]

    list_unsupported = [
        'block-device-mapping',
        'events',
        'hibernation',
        'identity-credentials',
        'managed-ssh-keys',
        'metrics',
        'network',
        'placement',
        'public-keys'
    ]

    def get_meta(option):

        if option in list_unsupported or option not in list_supported:
            print("Sorry, {} is not a supported option.".format(option))
            sys.exit(1)

        try:
            result = requests.get(ec2_meta_core + "/" + option)
            result = json.dumps({'result': result.content.decode()})
            return result
        except (requests.exceptions.ConnectTimeout) as rt_err:
            err_message = rt_err
        except (requests.exceptions.ConnectionError) as rc_err:
            err_message = rc_err

        sys.exit(err_message)

    parsed_option = example_input_option.lower()

    result = get_meta( parsed_option )

    print(result)
    