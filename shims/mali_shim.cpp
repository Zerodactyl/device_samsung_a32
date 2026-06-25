#include <android/log.h>
#include <stdarg.h>
#include <stdlib.h>

extern "C" __attribute__((visibility("default"), noreturn))
void _ZNSt3__122__libcpp_verbose_abortEPKcz(const char *fmt, ...) {
    va_list args;
    va_start(args, fmt);
    __android_log_vprint(ANDROID_LOG_FATAL, "MaliShim", fmt, args);
    va_end(args);
    abort();
}
