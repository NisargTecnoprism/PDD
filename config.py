video_path = r"/kaggle/input/meeting-w-surbhi/long_proper.mp4"
audio_output_dir = r"/kaggle/working/"
model_name = "large-v2"
doc_path = r"/kaggle/working/PDD_Document.docx"

GEMINI_API_KEY = "AIzaSyBdyWaRhXjfbIL7i3_c4H0Y_J3oCHrG5wI"  # Keep this safe

keywords = {
    "click": ["click", "press", "tap", "select", "choose", "hit", "push"],
    "submit": ["submit", "confirm", "send", "apply", "proceed", "finalize", "approve"],
    "open": ["open", "launch", "access", "start", "initiate", "run"],
    "navigate": ["navigate", "go to", "move to", "visit", "switch to", "redirect"],
    "type": ["type", "enter", "input", "write", "fill", "insert", "key in"],
    "scroll": ["scroll", "move down", "move up", "swipe", "browse", "drag down", "drag up"],
    "copy": ["copy", "duplicate", "clone", "replicate", "select and copy"],
    "paste": ["paste", "insert", "add", "attach", "drop", "transfer"],
    "cut": ["cut", "trim", "remove", "extract", "delete and move"],
    "delete": ["delete", "remove", "erase", "clear", "discard", "wipe"],
    "upload": ["upload", "attach", "send", "add file", "transfer"],
    "download": ["download", "save", "fetch", "retrieve", "get file"],
    "save": ["save", "store", "keep", "preserve", "record"],
    "move": ["move", "relocate", "transfer", "shift", "drag"],
    "resize": ["resize", "adjust", "change size", "scale", "stretch"],
    "minimize": ["minimize", "collapse", "hide", "shrink"],
    "maximize": ["maximize", "expand", "enlarge", "zoom"],
    "refresh": ["refresh", "reload", "update", "restart"],
    "close": ["close", "exit", "shut down", "terminate", "end"],
    "approve": ["approve", "authorize", "sign off", "validate", "confirm"],
    "reject": ["reject", "deny", "decline", "disapprove", "refuse"],
    "review": ["review", "analyze", "check", "evaluate", "inspect"],
    "create": ["create", "build", "generate", "produce", "construct"],
    "assign": ["assign", "allocate", "delegate", "give task", "designate"],
    "update": ["update", "modify", "change", "edit", "revise"],
    "cancel": ["cancel", "abort", "stop", "terminate", "withdraw"],
    "track": ["track", "monitor", "follow", "observe", "audit"],
    "notify": ["notify", "alert", "inform", "remind"],
    "attach": ["attach", "add", "link", "upload", "embed"],
    "download_file": ["download file", "save file", "fetch document", "retrieve file"],
    "upload_file": ["upload file", "send file", "add attachment", "transfer document"]
}
