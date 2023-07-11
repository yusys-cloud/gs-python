import gradio as gr
import pandas as pd

print(gr.__version__)

df = pd.DataFrame(columns=["prompt", "code","test"])

def collect_code_snippet(prompt, code,test):
    if code=="" or prompt=="" or test=="":
        return "None"
    global df
    df = df.append({"prompt": prompt, "code": code,"test":test}, ignore_index=True)
    df = df.drop_duplicates()
    df.to_csv("/home/ubuntu/yzq/datasets/yu/dataset-java-js-60.csv", index=False,mode="a")  # 保存数据集到 CSV 文件

    return df

iface = gr.Interface(
    fn=collect_code_snippet,
    inputs=["text", "text", "text"],
    outputs="text",
    title="benchmark代码评测集",
    description="录入java与js各30",
    allow_flagging=False,
    use_gradio_styles=False, 
    use_gradio_script=False,
    examples=[
        ["两个数相加的方法 add(int a,int b)","public static int add(int a, int b) {return a + b;}","@Test public void testAdd() { int result = Addition.add(2, 3); assertEquals(5, result);}"],
        ["/*Given a string s, count the number of uppercase vowels in even indices.For example:countUpper('aBCdEf') returns 1countUpper('abcdefg') returns 0countUpper('dBBE') returns 0*/const countUpper = (s) => {"
         ,"方法源码"
         ,"const testCountUpper = () => {console.assert(countUpper('aBCdEf') === 1)console.assert(countUpper('abcdefg') === 0)console.assert(countUpper('dBBE') === 0)}testCountUpper()"],
        ["根据使用习通过提示词能自动生成方法，如：import java.util.*;import java.lang.*;class Solution {/**Return n-th Fibonacci number.>>> fib(10)55>>> fib(1)1>>> fib(8)21*/public int fib(int n) {"
         ,"方法源码"
         , "测试用例，如：public class Main {public static void main(String[] args) {Solution s = new Solution();List<Boolean> correct = Arrays.asList(s.fib(10) == 55,s.fib(1) == 1,s.fib(8) == 21);if (correct.contains(false)) {throw new AssertionError();}}}"]]
)

# iface.launch()
iface.launch(auth=("m", "m"),server_port=7866)
