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
	char *out = priv->out;
	GetWindowText(hwnd, out, 500);
	if(strstr(out, priv->prefix) == out) {
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