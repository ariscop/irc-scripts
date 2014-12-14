#include <windows.h>

extern "C" {

struct _priv {
	char *out;
	char *prefix;
	bool success;
};

BOOL CALLBACK EnumWindowProc(HWND hwnd, LPARAM lp)
{
	struct _priv *priv = (struct _priv*)lp;
	wchar_t name[500];
	GetWindowTextW(hwnd, name, 500);
	WideCharToMultiByte(CP_UTF8, 0, name, -1, priv->out, 500, NULL, NULL);
	if(strstr(priv->out, priv->prefix) == priv->out) {
		priv->success = true;
		return FALSE;
	}
	return TRUE;
}

int __stdcall mircFindWindow(HWND mWnd, HWND aWnd, char *data, char *parms, BOOL show, 
					   BOOL nopause)
{
	struct _priv priv;
	char prefix[900];
	strcpy(prefix, data);
	priv.success = false;
	priv.out = data;
	priv.prefix = prefix;
	EnumWindows(EnumWindowProc, (LPARAM)&priv);
	if(!priv.success)
		data[0] = 0;
	return 3;
}

} //extern "C"
