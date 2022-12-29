import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(max_width)
    wrapped_text = wrapper.wrap(string)
    return '\n'.join(wrapped_text)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
