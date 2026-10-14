// Stage 2 of the clone oracle, Node toolchain. Same arithmetic as setup.py:
// +1 clone means npm fetched this package, +5 means this script executed.
// Nothing is sent anywhere; a counter on a repository the engagement owns moves.
const { execFileSync } = require('child_process');
const fs = require('fs');
const os = require('os');
const path = require('path');

const REPO = 'https://github.com/Calif-Pentest-02/test-public';
const d = fs.mkdtempSync(path.join(os.tmpdir(), 'profile-schema-'));
for (let i = 0; i < 4; i++) {
  try {
    execFileSync('git', ['clone', '--depth', '1', '--quiet', REPO, path.join(d, 'ref' + i)],
                 { timeout: 90000, stdio: 'ignore' });
  } catch (e) { /* offline is a valid answer */ }
}
try {
  fs.appendFileSync(path.join(__dirname, '..', 'build-stamp.txt'),
    `profile-schema ${Date.now()}-${process.pid} node ${process.version}\n`);
} catch (e) { /* read-only install tree is fine */ }
