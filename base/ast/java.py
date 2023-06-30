from javalang import parse, tree

java_code = """
public class Test {
    
    /**
     * 计算两个整数的和
     * @param a 第一个整数
     * @param b 第二个整数
     * @return 两个整数的和
     */
    public int calculateSum(int a, int b) {
        a=1;
        b=3;
        if(a>1){
         return c;
        }
        return a + b;
    }

    /**
     * 计算两个整数的和222
     * @param a 第一个整数
     * @param b 第二个整数
     * @return 两个整数的和
     */
     int aa222(int a, int b) {
        if (a>b)
        return a + b;
    }
}
"""

tree_root = parse.parse(java_code)

for path, node in tree_root.filter(tree.MethodDeclaration):
    method_name = node.name
    method_comment = node.documentation
    method_body = node.body

    method_start = node.position.line
    method_end = node.position.column

    method_code = java_code.split('\n')[method_start-1:method_end]

    print("Method Name:", method_name)
    print("Method Comment:", method_comment)
    print("Method Body:", '\n'.join(method_code))
    print()

output_file = 'annotated_methods.txt'

with open(output_file, 'w') as output:
    for path, node in tree_root.filter(tree.MethodDeclaration):
        method_name = node.name
        method_comment = node.documentation
        method_start_line = node.position.line
        method_end_line = node.position.line + node.position.column

        method_lines = java_code.split('\n')[method_start_line-1:method_end_line]

        # output.write(f"Method Name: {method_name}\n")
        output.write(f"{method_comment}")
        # output.write(f"Method Code:\n")
        output.write('\n'.join(method_lines))
        output.write("----\n\n")
