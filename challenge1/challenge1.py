key = "a"
test_object = {"a":{"b":{"c":"d"}}}

if __name__ == "__main__":

    def deep_value( haystack: dict ):

        for k, v in haystack.items():
            ## DEBUG
            # print(key)
            # print(k)
            # print(needle)

            if k == key:
                found = "Key {} found! Value: {}".format( key, haystack[k] )
                break

            if type(v) is dict:
                found = deep_value( v )
                break
            else:
                found = "Key {} could not be found!".format( key )
                break

        return found

    print( deep_value(test_object) )

exit(0)
