 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a//dev/null b/quote_app.py
index 0000000000000000000000000000000000000000..a8504aa04334cdef32a276a17427b1ffb2bc1546 100644
--- a//dev/null
+++ b/quote_app.py
@@ -0,0 +1,25 @@
+import random
+
+QUOTES = [
+    "The only way to do great work is to love what you do. – Steve Jobs",
+    "Life is what happens when you're busy making other plans. – John Lennon",
+    "Do not watch the clock. Do what it does. Keep going. – Sam Levenson",
+    "Success is not final, failure is not fatal: it is the courage to continue that counts. – Winston Churchill",
+    "Believe you can and you're halfway there. – Theodore Roosevelt",
+]
+
+
+def get_random_quote() -> str:
+    """Return a random quote from the predefined list."""
+    if not QUOTES:
+        raise ValueError("No quotes available")
+    return random.choice(QUOTES)
+
+
+def main() -> None:
+    """Print a random quote to the console."""
+    print(get_random_quote())
+
+
+if __name__ == "__main__":
+    main()
 
EOF
)
