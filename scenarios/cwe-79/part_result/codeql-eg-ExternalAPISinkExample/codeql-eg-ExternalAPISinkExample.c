#include <stdio.h>
#include <stdlib.h>

#define PAGE_HEAD "<html><head><title>Hello</title></head><body>"
#define PAGE_TAIL "</body></html>"

// 这个函数用于转义HTML中的特殊字符，但在这里它只返回 "safe"，应该实现真正的转义函数以防止 XSS 攻击
char* escape_html(char* input) {
  return "safe";
}

void http_hello_page(const char *url, const char *method, FILE* request, FILE* response) {
  char username[1024];
  fgets(username, 1024, request);
  char outputbuf[2048]; // 增加缓冲区大小，以容纳更长的响应

  // 构造响应，显示 "hello, [username]"
  // 使用 PAGE 定义
  snprintf(outputbuf, sizeof(outputbuf), "%s<h1>Hello, %s</h1>%s", PAGE_HEAD, escape_html(username), PAGE_TAIL);
  
  fputs(outputbuf, response);
}