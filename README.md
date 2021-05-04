The Command Line Murders
========================

	.OOOOOOOOOOOOOOO @@                                   @@ OOOOOOOOOOOOOOOO.
	OOOOOOOOOOOOOOOO @@                                    @@ OOOOOOOOOOOOOOOO
	OOOOOOOOOO'''''' @@                                    @@ ```````OOOOOOOOO
	OOOOO'' aaa@@@@@@@@@@@@@@@@@@@@"""                   """""""""@@aaaa `OOOO
	OOOOO,""""@@@@@@@@@@@@@@""""                                     a@"" OOOA
	OOOOOOOOOoooooo,                                            |OOoooooOOOOOS
	OOOOOOOOOOOOOOOOo,                                          |OOOOOOOOOOOOC
	OOOOOOOOOOOOOOOOOO                                         ,|OOOOOOOOOOOOI
	OOOOOOOOOOOOOOOOOO @          THE                          |OOOOOOOOOOOOOI
	OOOOOOOOOOOOOOOOO'@           COMMAND                      OOOOOOOOOOOOOOb
	OOOOOOOOOOOOOOO'a'            LINE                         |OOOOOOOOOOOOOy
	OOOOOOOOOOOOOO''              MURDERS                      aa`OOOOOOOOOOOP
	OOOOOOOOOOOOOOb,..                                          `@aa``OOOOOOOh
	OOOOOOOOOOOOOOOOOOo                                           `@@@aa OOOOo
	OOOOOOOOOOOOOOOOOOO|                                             @@@ OOOOe
	OOOOOOOOOOOOOOOOOOO@                               aaaaaaa       @@',OOOOn
	OOOOOOOOOOOOOOOOOOO@                        aaa@@@@@@@@""        @@ OOOOOi
	OOOOOOOOOO~~ aaaaaa"a                 aaa@@@@@@@@@@""            @@ OOOOOx
	OOOOOO aaaa@"""""""" ""            @@@@@@@@@@@@""               @@@|`OOOO'
	OOOOOOOo`@@a                  aa@@  @@@@@@@""         a@        @@@@ OOOO9
	OOOOOOO'  `@@a               @@a@@   @@""           a@@   a     |@@@ OOOO3
	`OOOO'       `@    aa@@       aaa"""          @a        a@     a@@@',OOOO'


There's been a murder in Terminal City, and TCPD needs your help.

To figure out whodunit, you need access to a command line.

## Getting Started

* Fork and clone this repo.
* Once the repo has been cloned...
  * Open a Terminal
  * Go to the location of the files
  * Start by reading the file 'instructions'.

One way you can do this is with the command:
```
cat instructions
```

* To get started on how to use the command line, open cheatsheet.md.
  * Again, you can use the `cat` command to do this
* Don't use a text editor to view any files except these instructions, the cheatsheet, and hints.

## Deliverables

* Create a file called `solution.txt` in this repo
* Copy/paste the following:

1. The commands you used to get the solution (hint: run `history` for a list of the commands you ran).
2. The name of the killer.

* Commit your solution file
* Push your changes to your forked repo
* Create a pull request to submit your deliverable
    1  git init
    2  cd
    3  cd list
    4  list
    5  git --version
    6  git init
    7  xcode-select --install
    8  git --version
    9  $ git init
   10  git init
   11  cd list
   12  cd users
   13  ls list
   14  ls
   15  $
   16  %
   17  $
   18  %
   19  pwd
   20  ls -a
   21  cd .git
   22  pwd .git
   23  cd ~
   24  pwd
   25  cd .git
   26  pwd
   27  cd ga-blog
   28  ls
   29  cd desktop
   30  ls
   31  ls desktop
   32  ls
   33  pwd
   34  mkdir GA-Blog
   35  cd ga-blog
   36  touch index.heml style.css
   37  rm index.heml
   38  rmdir ga-blog
   39  rmdir GA-Blog
   40  cd
   41  pwd
   42  rm -r ga-blog
   43  rm -r GA-Blog
   44  mkdir myfolder
   45  rm -r myfolder
   46  rm -r ~/ga-blog
   47  rm -r ~/GA-Blog
   48  pwd
   49  ls
   50  cd desktop
   51  rmdir GA-Blog
   52  rmdir ~/GA-Blog
   53  rm -r ga-blog
   54  mkdir GA-Blog
   55  cd ga-blog
   56  git init
   57  pwd
   58  ls -a
   59  git status
   60  touch post.txt
   61  git add post.txt
   62  git status
   63  git add .
   64  git status
   65  git commit -m created a new post.txt file
   66  git config --global user.name miknayr
   67  git config --global user.email ryan@miknayr.com
   68  git status
   69  git add post.txt
   70  git commit -m posting txt file
   71  git log
   72  mkdir git-practice
   73  cd git-practice
   74  git init
   75  touch textfile.txt
   76  ls -a
   77  touch README.txt
   78  git status
   79  git commit -m two files of test text
   80  git log
   81  git add readme.txt
   82  git add textfile.txt
   83  git commit -m two files of test text
   84  git log
   85  git clone https://github.com/miknayr/Hello-World.git
   86  git add readme
   87  cd hello-world
   88  git add README
   89  git commit -m added ryan to readme
   90  git push origin master
   91  echo 
   92  echo /bin/zsh
   93  chsh -s /bin/zsh
   94  /bin/bash -c #!/bin/bash set -u abort() { printf "%s
" "$@" exit 1 } if [ -z "${BASH_VERSION:-}" ]; then abort "Bash is required to interpret this script." fi # Check if script is run non-interactively (e.g. CI) # If it is run non-interactively we should not prompt for passwords. if [[ ! -t 0 || -n "${CI-}" ]]; then NONINTERACTIVE=1 fi # First check OS. OS="$(uname)" if [[ "$OS" == "Linux" ]]; then HOMEBREW_ON_LINUX=1 elif [[ "$OS" != "Darwin" ]]; then abort "Homebrew is only supported on macOS and Linux." fi # Required installation paths. To install elsewhere (which is unsupported) # you can untar https://github.com/Homebrew/brew/tarball/master # anywhere you like. if [[ -z "${HOMEBREW_ON_LINUX-}" ]]; then UNAME_MACHINE="$(/usr/bin/uname -m)" if [[ "$UNAME_MACHINE" == "arm64" ]]; then # On ARM macOS, this script installs to /opt/homebrew only HOMEBREW_PREFIX="/opt/homebrew" HOMEBREW_REPOSITORY="${HOMEBREW_PREFIX}" else # On Intel macOS, this script installs to /usr/local only HOMEBREW_PREFIX="/usr/local" HOMEBREW_REPOSITORY="${HOMEBREW_PREFIX}/Homebrew" fi HOMEBREW_CACHE="${HOME}/Library/Caches/Homebrew" HOMEBREW_CORE_DEFAULT_GIT_REMOTE="https://github.com/Homebrew/homebrew-core" STAT="stat -f" CHOWN="/usr/sbin/chown" CHGRP="/usr/bin/chgrp" GROUP="admin" TOUCH="/usr/bin/touch" else UNAME_MACHINE="$(uname -m)" # On Linux, it installs to /home/linuxbrew/.linuxbrew if you have sudo access # and ~/.linuxbrew (which is unsupported) if run interactively. HOMEBREW_PREFIX_DEFAULT="/home/linuxbrew/.linuxbrew" HOMEBREW_CACHE="${HOME}/.cache/Homebrew" HOMEBREW_CORE_DEFAULT_GIT_REMOTE="https://github.com/Homebrew/linuxbrew-core" STAT="stat --printf" CHOWN="/bin/chown" CHGRP="/bin/chgrp" GROUP="$(id -gn)" TOUCH="/bin/touch" fi HOMEBREW_BREW_DEFAULT_GIT_REMOTE="https://github.com/Homebrew/brew" # Use remote URLs of Homebrew repositories from environment if set. HOMEBREW_BREW_GIT_REMOTE="${HOMEBREW_BREW_GIT_REMOTE:-"${HOMEBREW_BREW_DEFAULT_GIT_REMOTE}"}" HOMEBREW_CORE_GIT_REMOTE="${HOMEBREW_CORE_GIT_REMOTE:-"${HOMEBREW_CORE_DEFAULT_GIT_REMOTE}"}" # The URLs with and without the '.git' suffix are the same Git remote. Do not prompt. if [[ "$HOMEBREW_BREW_GIT_REMOTE" == "${HOMEBREW_BREW_DEFAULT_GIT_REMOTE}.git" ]]; then HOMEBREW_BREW_GIT_REMOTE="${HOMEBREW_BREW_DEFAULT_GIT_REMOTE}" fi if [[ "$HOMEBREW_CORE_GIT_REMOTE" == "${HOMEBREW_CORE_DEFAULT_GIT_REMOTE}.git" ]]; then HOMEBREW_CORE_GIT_REMOTE="${HOMEBREW_CORE_DEFAULT_GIT_REMOTE}" fi export HOMEBREW_{BREW,CORE}_GIT_REMOTE # TODO: bump version when new macOS is released or announced MACOS_NEWEST_UNSUPPORTED="12.0" # TODO: bump version when new macOS is released MACOS_OLDEST_SUPPORTED="10.14" # For Homebrew on Linux REQUIRED_RUBY_VERSION=2.6 # https://github.com/Homebrew/brew/pull/6556 REQUIRED_GLIBC_VERSION=2.13 # https://docs.brew.sh/Homebrew-on-Linux#requirements # no analytics during installation export HOMEBREW_NO_ANALYTICS_THIS_RUN=1 export HOMEBREW_NO_ANALYTICS_MESSAGE_OUTPUT=1 # string formatters if [[ -t 1 ]]; then tty_escape() { printf "[%sm" "$1"; } else tty_escape() { :; } fi tty_mkbold() { tty_escape "1;$1"; } tty_underline="$(tty_escape "4;39")" tty_blue="$(tty_mkbold 34)" tty_red="$(tty_mkbold 31)" tty_bold="$(tty_mkbold 39)" tty_reset="$(tty_escape 0)" have_sudo_access() { local -a args if [[ -n "${SUDO_ASKPASS-}" ]]; then args=("-A") elif [[ -n "${NONINTERACTIVE-}" ]]; then args=("-n") fi if [[ -z "${HAVE_SUDO_ACCESS-}" ]]; then if [[ -n "${args[*]-}" ]]; then SUDO="/usr/bin/sudo ${args[*]}" else SUDO="/usr/bin/sudo" fi if [[ -n "${NONINTERACTIVE-}" ]]; then ${SUDO} -l mkdir &>/dev/null else ${SUDO} -v && ${SUDO} -l mkdir &>/dev/null fi HAVE_SUDO_ACCESS="$?" fi if [[ -z "${HOMEBREW_ON_LINUX-}" ]] && [[ "$HAVE_SUDO_ACCESS" -ne 0 ]]; then abort "Need sudo access on macOS (e.g. the user $USER needs to be an Administrator)!" fi return "$HAVE_SUDO_ACCESS" } shell_join() { local arg printf "%s" "$1" shift for arg in "$@"; do printf " " printf "%s" "${arg// /\ }" done } chomp() { printf "%s" "${1/"$'
'"/}" } ohai() { printf "${tty_blue}==>${tty_bold} %s${tty_reset}
" "$(shell_join "$@")" } warn() { printf "${tty_red}Warning${tty_reset}: %s
" "$(chomp "$1")" } execute() { if ! "$@"; then abort "$(printf "Failed during: %s" "$(shell_join "$@")")" fi } execute_sudo() { local -a args=("$@") if have_sudo_access; then if [[ -n "${SUDO_ASKPASS-}" ]]; then args=("-A" "${args[@]}") fi ohai "/usr/bin/sudo" "${args[@]}" execute "/usr/bin/sudo" "${args[@]}" else ohai "${args[@]}" execute "${args[@]}" fi } getc() { local save_state save_state=$(/bin/stty -g) /bin/stty raw -echo IFS= read -r -n 1 -d '' "$@" /bin/stty "$save_state" } ring_bell() { # Use the shell's audible bell. if [[ -t 1 ]]; then printf "" fi } wait_for_user() { local c echo echo "Press RETURN to continue or any other key to abort" getc c # we test for  and 
 because some stuff does  instead if ! [[ "$c" == $'' || "$c" == $'
' ]]; then exit 1 fi } major_minor() { echo "${1%%.*}.$(x="${1#*.}"; echo "${x%%.*}")" } version_gt() { [[ "${1%.*}" -gt "${2%.*}" ]] || [[ "${1%.*}" -eq "${2%.*}" && "${1#*.}" -gt "${2#*.}" ]] } version_ge() { [[ "${1%.*}" -gt "${2%.*}" ]] || [[ "${1%.*}" -eq "${2%.*}" && "${1#*.}" -ge "${2#*.}" ]] } version_lt() { [[ "${1%.*}" -lt "${2%.*}" ]] || [[ "${1%.*}" -eq "${2%.*}" && "${1#*.}" -lt "${2#*.}" ]] } should_install_command_line_tools() { if [[ -n "${HOMEBREW_ON_LINUX-}" ]]; then return 1 fi if version_gt "$macos_version" "10.13"; then ! [[ -e "/Library/Developer/CommandLineTools/usr/bin/git" ]] else ! [[ -e "/Library/Developer/CommandLineTools/usr/bin/git" ]] || ! [[ -e "/usr/include/iconv.h" ]] fi } get_permission() { $STAT "%A" "$1" } user_only_chmod() { [[ -d "$1" ]] && [[ "$(get_permission "$1")" != "755" ]] } exists_but_not_writable() { [[ -e "$1" ]] && ! [[ -r "$1" && -w "$1" && -x "$1" ]] } get_owner() { $STAT "%u" "$1" } file_not_owned() { [[ "$(get_owner "$1")" != "$(id -u)" ]] } get_group() { $STAT "%g" "$1" } file_not_grpowned() { [[ " $(id -G "$USER") " != *" $(get_group "$1") "* ]] } # Please sync with 'test_ruby()' in 'Library/Homebrew/utils/ruby.sh' from Homebrew/brew repository. test_ruby() { if [[ ! -x $1 ]] then return 1 fi "$1" --enable-frozen-string-literal --disable=gems,did_you_mean,rubyopt -rrubygems -e \ "abort if Gem::Version.new(RUBY_VERSION.to_s.dup).to_s.split('.').first(2) != \ Gem::Version.new('$REQUIRED_RUBY_VERSION').to_s.split('.').first(2)" 2>/dev/null } no_usable_ruby() { local ruby_exec IFS=$'
' # Do word splitting on new lines only for ruby_exec in $(which -a ruby 2>/dev/null); do if test_ruby "$ruby_exec"; then IFS=$' 	
' # Restore IFS to its default value return 1 fi done IFS=$' 	
' # Restore IFS to its default value return 0 } outdated_glibc() { local glibc_version glibc_version=$(ldd --version | head -n1 | grep -o '[0-9.]*$' | grep -o '^[0-9]\+\.[0-9]\+') version_lt "$glibc_version" "$REQUIRED_GLIBC_VERSION" } if [[ -n "${HOMEBREW_ON_LINUX-}" ]] && no_usable_ruby && outdated_glibc then abort "$(cat <<-EOFABORT Homebrew requires Ruby $REQUIRED_RUBY_VERSION which was not found on your system. Homebrew portable Ruby requires Glibc version $REQUIRED_GLIBC_VERSION or newer, and your Glibc version is too old. See ${tty_underline}https://docs.brew.sh/Homebrew-on-Linux#requirements${tty_reset} Install Ruby $REQUIRED_RUBY_VERSION and add its location to your PATH. EOFABORT )" fi # USER isn't always set so provide a fall back for the installer and subprocesses. if [[ -z "${USER-}" ]]; then USER="$(chomp "$(id -un)")" export USER fi # Invalidate sudo timestamp before exiting (if it wasn't active before). if ! /usr/bin/sudo -n -v 2>/dev/null; then trap '/usr/bin/sudo -k' EXIT fi # Things can fail later if `pwd` doesn't exist. # Also sudo prints a warning message for no good reason cd "/usr" || exit 1 ####################################################################### script if ! command -v git >/dev/null; then abort "$(cat <<EOABORT You must install Git before installing Homebrew. See: ${tty_underline}https://docs.brew.sh/Installation${tty_reset} EOABORT )" fi if ! command -v curl >/dev/null; then abort "$(cat <<EOABORT You must install cURL before installing Homebrew. See: ${tty_underline}https://docs.brew.sh/Installation${tty_reset} EOABORT )" fi # shellcheck disable=SC2016 ohai 'Checking for `sudo` access (which may request your password).' if [[ -z "${HOMEBREW_ON_LINUX-}" ]]; then have_sudo_access else if [[ -n "${NONINTERACTIVE-}" ]] || [[ -w "${HOMEBREW_PREFIX_DEFAULT}" ]] || [[ -w "/home/linuxbrew" ]] || [[ -w "/home" ]]; then HOMEBREW_PREFIX="$HOMEBREW_PREFIX_DEFAULT" else trap exit SIGINT if ! /usr/bin/sudo -n -v &>/dev/null; then ohai "Select the Homebrew installation directory" echo "- ${tty_bold}Enter your password${tty_reset} to install to ${tty_underline}${HOMEBREW_PREFIX_DEFAULT}${tty_reset} (${tty_bold}recommended${tty_reset})" echo "- ${tty_bold}Press Control-D${tty_reset} to install to ${tty_underline}$HOME/.linuxbrew${tty_reset}" echo "- ${tty_bold}Press Control-C${tty_reset} to cancel installation" fi if have_sudo_access; then HOMEBREW_PREFIX="$HOMEBREW_PREFIX_DEFAULT" else HOMEBREW_PREFIX="$HOME/.linuxbrew" fi trap - SIGINT fi HOMEBREW_REPOSITORY="${HOMEBREW_PREFIX}/Homebrew" fi HOMEBREW_CORE="${HOMEBREW_REPOSITORY}/Library/Taps/homebrew/homebrew-core" if [[ "${EUID:-${UID}}" == "0" ]]; then abort "Don't run this as root!" elif [[ -d "${HOMEBREW_PREFIX}" && ! -x "${HOMEBREW_PREFIX}" ]]; then abort "$(cat <<EOABORT The Homebrew prefix, ${HOMEBREW_PREFIX}, exists but is not searchable. If this is not intentional, please restore the default permissions and try running the installer again: sudo chmod 775 ${HOMEBREW_PREFIX} EOABORT )" fi if [[ -z "${HOMEBREW_ON_LINUX-}" ]]; then # On macOS, support 64-bit Intel and ARM if [[ "$UNAME_MACHINE" != "arm64" ]] && [[ "$UNAME_MACHINE" != "x86_64" ]]; then abort "Homebrew is only supported on Intel and ARM processors!" fi else # On Linux, support only 64-bit Intel if [[ "$UNAME_MACHINE" == "arm64" ]]; then abort "$(cat <<EOABORT Homebrew on Linux is not supported on ARM processors. You can try an alternate installation method instead: ${tty_underline}https://docs.brew.sh/Homebrew-on-Linux#arm${tty_reset} EOABORT )" elif [[ "$UNAME_MACHINE" != "x86_64" ]]; then abort "Homebrew on Linux is only supported on Intel processors!" fi fi if [[ -z "${HOMEBREW_ON_LINUX-}" ]]; then macos_version="$(major_minor "$(/usr/bin/sw_vers -productVersion)")" if version_lt "$macos_version" "10.7"; then abort "$(cat <<EOABORT Your Mac OS X version is too old. See: ${tty_underline}https://github.com/mistydemeo/tigerbrew${tty_reset} EOABORT )" elif version_lt "$macos_version" "10.10"; then abort "Your OS X version is too old" elif version_ge "$macos_version" "$MACOS_NEWEST_UNSUPPORTED" || \ version_lt "$macos_version" "$MACOS_OLDEST_SUPPORTED"; then who="We" what="" if version_ge "$macos_version" "$MACOS_NEWEST_UNSUPPORTED"; then what="pre-release version" else who+=" (and Apple)" what="old version" fi ohai "You are using macOS ${macos_version}." ohai "${who} do not provide support for this ${what}." echo "$(cat <<EOS This installation may not succeed. After installation, you will encounter build failures with some formulae. Please create pull requests instead of asking for help on Homebrew\'s GitHub, Twitter or IRC. You are responsible for resolving any issues you experience while you are running this ${what}. EOS ) " fi fi ohai "This script will install:" echo "${HOMEBREW_PREFIX}/bin/brew" echo "${HOMEBREW_PREFIX}/share/doc/homebrew" echo "${HOMEBREW_PREFIX}/share/man/man1/brew.1" echo "${HOMEBREW_PREFIX}/share/zsh/site-functions/_brew" echo "${HOMEBREW_PREFIX}/etc/bash_completion.d/brew" echo "${HOMEBREW_REPOSITORY}" # Keep relatively in sync with # https://github.com/Homebrew/brew/blob/master/Library/Homebrew/keg.rb directories=(bin etc include lib sbin share opt var Frameworks etc/bash_completion.d lib/pkgconfig share/aclocal share/doc share/info share/locale share/man share/man/man1 share/man/man2 share/man/man3 share/man/man4 share/man/man5 share/man/man6 share/man/man7 share/man/man8 var/log var/homebrew var/homebrew/linked bin/brew) group_chmods=() for dir in "${directories[@]}"; do if exists_but_not_writable "${HOMEBREW_PREFIX}/${dir}"; then group_chmods+=("${HOMEBREW_PREFIX}/${dir}") fi done # zsh refuses to read from these directories if group writable directories=(share/zsh share/zsh/site-functions) zsh_dirs=() for dir in "${directories[@]}"; do zsh_dirs+=("${HOMEBREW_PREFIX}/${dir}") done directories=(bin etc include lib sbin share var opt share/zsh share/zsh/site-functions var/homebrew var/homebrew/linked Cellar Caskroom Frameworks) mkdirs=() for dir in "${directories[@]}"; do if ! [[ -d "${HOMEBREW_PREFIX}/${dir}" ]]; then mkdirs+=("${HOMEBREW_PREFIX}/${dir}") fi done user_chmods=() if [[ "${#zsh_dirs[@]}" -gt 0 ]]; then for dir in "${zsh_dirs[@]}"; do if user_only_chmod "${dir}"; then user_chmods+=("${dir}") fi done fi chmods=() if [[ "${#group_chmods[@]}" -gt 0 ]]; then chmods+=("${group_chmods[@]}") fi if [[ "${#user_chmods[@]}" -gt 0 ]]; then chmods+=("${user_chmods[@]}") fi chowns=() chgrps=() if [[ "${#chmods[@]}" -gt 0 ]]; then for dir in "${chmods[@]}"; do if file_not_owned "${dir}"; then chowns+=("${dir}") fi if file_not_grpowned "${dir}"; then chgrps+=("${dir}") fi done fi if [[ "${#group_chmods[@]}" -gt 0 ]]; then ohai "The following existing directories will be made group writable:" printf "%s
" "${group_chmods[@]}" fi if [[ "${#user_chmods[@]}" -gt 0 ]]; then ohai "The following existing directories will be made writable by user only:" printf "%s
" "${user_chmods[@]}" fi if [[ "${#chowns[@]}" -gt 0 ]]; then ohai "The following existing directories will have their owner set to ${tty_underline}${USER}${tty_reset}:" printf "%s
" "${chowns[@]}" fi if [[ "${#chgrps[@]}" -gt 0 ]]; then ohai "The following existing directories will have their group set to ${tty_underline}${GROUP}${tty_reset}:" printf "%s
" "${chgrps[@]}" fi if [[ "${#mkdirs[@]}" -gt 0 ]]; then ohai "The following new directories will be created:" printf "%s
" "${mkdirs[@]}" fi if should_install_command_line_tools; then ohai "The Xcode Command Line Tools will be installed." fi non_default_repos="" additional_shellenv_commands=() if [[ "$HOMEBREW_BREW_DEFAULT_GIT_REMOTE" != "$HOMEBREW_BREW_GIT_REMOTE" ]]; then ohai "HOMEBREW_BREW_GIT_REMOTE is set to a non-default URL:" echo "${tty_underline}${HOMEBREW_BREW_GIT_REMOTE}${tty_reset} will be used for Homebrew/brew Git remote." non_default_repos="Homebrew/brew" additional_shellenv_commands+=("export HOMEBREW_BREW_GIT_REMOTE=\"$HOMEBREW_BREW_GIT_REMOTE\"") fi if [[ "$HOMEBREW_CORE_DEFAULT_GIT_REMOTE" != "$HOMEBREW_CORE_GIT_REMOTE" ]]; then ohai "HOMEBREW_CORE_GIT_REMOTE is set to a non-default URL:" echo "${tty_underline}${HOMEBREW_CORE_GIT_REMOTE}${tty_reset} will be used for Homebrew/core Git remote." non_default_repos="${non_default_repos:-}${non_default_repos:+ and }Homebrew/core" additional_shellenv_commands+=("export HOMEBREW_CORE_GIT_REMOTE=\"$HOMEBREW_CORE_GIT_REMOTE\"") fi if [[ -z "${NONINTERACTIVE-}" ]]; then ring_bell wait_for_user fi if [[ -d "${HOMEBREW_PREFIX}" ]]; then if [[ "${#chmods[@]}" -gt 0 ]]; then execute_sudo "/bin/chmod" "u+rwx" "${chmods[@]}" fi if [[ "${#group_chmods[@]}" -gt 0 ]]; then execute_sudo "/bin/chmod" "g+rwx" "${group_chmods[@]}" fi if [[ "${#user_chmods[@]}" -gt 0 ]]; then execute_sudo "/bin/chmod" "755" "${user_chmods[@]}" fi if [[ "${#chowns[@]}" -gt 0 ]]; then execute_sudo "$CHOWN" "$USER" "${chowns[@]}" fi if [[ "${#chgrps[@]}" -gt 0 ]]; then execute_sudo "$CHGRP" "$GROUP" "${chgrps[@]}" fi else execute_sudo "/bin/mkdir" "-p" "${HOMEBREW_PREFIX}" if [[ -z "${HOMEBREW_ON_LINUX-}" ]]; then execute_sudo "$CHOWN" "root:wheel" "${HOMEBREW_PREFIX}" else execute_sudo "$CHOWN" "$USER:$GROUP" "${HOMEBREW_PREFIX}" fi fi if [[ "${#mkdirs[@]}" -gt 0 ]]; then execute_sudo "/bin/mkdir" "-p" "${mkdirs[@]}" execute_sudo "/bin/chmod" "g+rwx" "${mkdirs[@]}" execute_sudo "$CHOWN" "$USER" "${mkdirs[@]}" execute_sudo "$CHGRP" "$GROUP" "${mkdirs[@]}" fi if ! [[ -d "${HOMEBREW_REPOSITORY}" ]]; then execute_sudo "/bin/mkdir" "-p" "${HOMEBREW_REPOSITORY}" fi execute_sudo "$CHOWN" "-R" "$USER:$GROUP" "${HOMEBREW_REPOSITORY}" if ! [[ -d "${HOMEBREW_CACHE}" ]]; then if [[ -z "${HOMEBREW_ON_LINUX-}" ]]; then execute_sudo "/bin/mkdir" "-p" "${HOMEBREW_CACHE}" else execute "/bin/mkdir" "-p" "${HOMEBREW_CACHE}" fi fi if exists_but_not_writable "${HOMEBREW_CACHE}"; then execute_sudo "/bin/chmod" "g+rwx" "${HOMEBREW_CACHE}" fi if file_not_owned "${HOMEBREW_CACHE}"; then execute_sudo "$CHOWN" "-R" "$USER" "${HOMEBREW_CACHE}" fi if file_not_grpowned "${HOMEBREW_CACHE}"; then execute_sudo "$CHGRP" "-R" "$GROUP" "${HOMEBREW_CACHE}" fi if [[ -d "${HOMEBREW_CACHE}" ]]; then execute "$TOUCH" "${HOMEBREW_CACHE}/.cleaned" fi if should_install_command_line_tools && version_ge "$macos_version" "10.13"; then ohai "Searching online for the Command Line Tools" # This temporary file prompts the 'softwareupdate' utility to list the Command Line Tools clt_placeholder="/tmp/.com.apple.dt.CommandLineTools.installondemand.in-progress" execute_sudo "$TOUCH" "$clt_placeholder" clt_label_command="/usr/sbin/softwareupdate -l | grep -B 1 -E 'Command Line Tools' | awk -F'*' '/^ *\*/ {print \$2}' | sed -e 's/^ *Label: //' -e 's/^ *//' | sort -V | tail -n1" clt_label="$(chomp "$(/bin/bash -c "$clt_label_command")")" if [[ -n "$clt_label" ]]; then ohai "Installing $clt_label" execute_sudo "/usr/sbin/softwareupdate" "-i" "$clt_label" execute_sudo "/bin/rm" "-f" "$clt_placeholder" execute_sudo "/usr/bin/xcode-select" "--switch" "/Library/Developer/CommandLineTools" fi fi # Headless install may have failed, so fallback to original 'xcode-select' method if should_install_command_line_tools && test -t 0; then ohai "Installing the Command Line Tools (expect a GUI popup):" execute_sudo "/usr/bin/xcode-select" "--install" echo "Press any key when the installation has completed." getc execute_sudo "/usr/bin/xcode-select" "--switch" "/Library/Developer/CommandLineTools" fi if [[ -z "${HOMEBREW_ON_LINUX-}" ]] && ! output="$(/usr/bin/xcrun clang 2>&1)" && [[ "$output" == *"license"* ]]; then abort "$(cat <<EOABORT You have not agreed to the Xcode license. Before running the installer again please agree to the license by opening Xcode.app or running: sudo xcodebuild -license EOABORT )" fi ohai "Downloading and installing Homebrew..." ( cd "${HOMEBREW_REPOSITORY}" >/dev/null || return # we do it in four steps to avoid merge errors when reinstalling execute "git" "init" "-q" # "git remote add" will fail if the remote is defined in the global config execute "git" "config" "remote.origin.url" "${HOMEBREW_BREW_GIT_REMOTE}" execute "git" "config" "remote.origin.fetch" "+refs/heads/*:refs/remotes/origin/*" # ensure we don't munge line endings on checkout execute "git" "config" "core.autocrlf" "false" execute "git" "fetch" "--force" "origin" execute "git" "fetch" "--force" "--tags" "origin" execute "git" "reset" "--hard" "origin/master" if [[ "${HOMEBREW_REPOSITORY}" != "${HOMEBREW_PREFIX}" ]]; then execute "ln" "-sf" "${HOMEBREW_REPOSITORY}/bin/brew" "${HOMEBREW_PREFIX}/bin/brew" fi if [[ ! -d "${HOMEBREW_CORE}" ]]; then ohai "Tapping homebrew/core" ( execute "/bin/mkdir" "-p" "${HOMEBREW_CORE}" cd "${HOMEBREW_CORE}" >/dev/null || return execute "git" "init" "-q" execute "git" "config" "remote.origin.url" "${HOMEBREW_CORE_GIT_REMOTE}" execute "git" "config" "remote.origin.fetch" "+refs/heads/*:refs/remotes/origin/*" execute "git" "config" "core.autocrlf" "false" execute "git" "fetch" "--force" "origin" "refs/heads/master:refs/remotes/origin/master" execute "git" "remote" "set-head" "origin" "--auto" >/dev/null execute "git" "reset" "--hard" "origin/master" cd "${HOMEBREW_REPOSITORY}" >/dev/null || return ) || exit 1 fi execute "${HOMEBREW_PREFIX}/bin/brew" "update" "--force" "--quiet" ) || exit 1 if [[ ":${PATH}:" != *":${HOMEBREW_PREFIX}/bin:"* ]]; then warn "${HOMEBREW_PREFIX}/bin is not in your PATH." fi ohai "Installation successful!" echo ring_bell # Use an extra newline and bold to avoid this being missed. ohai "Homebrew has enabled anonymous aggregate formulae and cask analytics." echo "$(cat <<EOS ${tty_bold}Read the analytics documentation (and how to opt-out) here: ${tty_underline}https://docs.brew.sh/Analytics${tty_reset} No analytics data has been sent yet (or will be during this \`install\` run). EOS ) " ohai "Homebrew is run entirely by unpaid volunteers. Please consider donating:" echo "$(cat <<EOS ${tty_underline}https://github.com/Homebrew/brew#donations${tty_reset} EOS ) " ( cd "${HOMEBREW_REPOSITORY}" >/dev/null || return execute "git" "config" "--replace-all" "homebrew.analyticsmessage" "true" execute "git" "config" "--replace-all" "homebrew.caskanalyticsmessage" "true" ) || exit 1 ohai "Next steps:" case "$SHELL" in */bash*) if [[ -r "$HOME/.bash_profile" ]]; then shell_profile="$HOME/.bash_profile" else shell_profile="$HOME/.profile" fi ;; */zsh*) shell_profile="$HOME/.zprofile" ;; *) shell_profile="$HOME/.profile" ;; esac if [[ "$UNAME_MACHINE" == "arm64" ]] || [[ -n "${HOMEBREW_ON_LINUX-}" ]]; then cat <<EOS - Add Homebrew to your ${tty_bold}PATH${tty_reset} in ${tty_underline}${shell_profile}${tty_reset}: echo 'eval "\$(${HOMEBREW_PREFIX}/bin/brew shellenv)"' >> ${shell_profile} eval "\$(${HOMEBREW_PREFIX}/bin/brew shellenv)" EOS fi if [[ -n "${non_default_repos}" ]]; then s="" if [[ "${#additional_shellenv_commands[@]}" -gt 1 ]]; then s="s" fi echo "- Add the non-default Git remote${s} for ${non_default_repos} in ${tty_underline}${shell_profile}${tty_reset}:" printf " echo '%s' >> ${shell_profile}
" "${additional_shellenv_commands[@]}" printf " %s
" "${additional_shellenv_commands[@]}" fi echo "- Run \`brew help\` to get started" echo "- Further documentation: " echo " ${tty_underline}https://docs.brew.sh${tty_reset}" if [[ -n "${HOMEBREW_ON_LINUX-}" ]]; then echo "- Install the Homebrew dependencies if you have sudo access:" if [[ $(command -v apt-get) ]]; then echo " sudo apt-get install build-essential" elif [[ $(command -v yum) ]]; then echo " sudo yum groupinstall 'Development Tools'" elif [[ $(command -v pacman) ]]; then echo " sudo pacman -S base-devel" elif [[ $(command -v apk) ]]; then echo " sudo apk add build-base" fi cat <<EOS See ${tty_underline}https://docs.brew.sh/linux${tty_reset} for more information - We recommend that you install GCC: brew install gcc EOS fi
   95  brew install zsh
   96  brew-v
   97  brew -v
   98  brew -update
   99  brew commands
  100  brew -upgrade
  101  brew install zsh
  102  chsh -s /bin/zsh
  103  chsh -s /bin/zsh
  104  echo /bin/zsh
  105  sh -c #!/bin/sh # # This script should be run via curl: # sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" # or via wget: # sh -c "$(wget -qO- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" # or via fetch: # sh -c "$(fetch -o - https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" # # As an alternative, you can first download the install script and run it afterwards: # wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh # sh install.sh # # You can tweak the install behavior by setting variables when running the script. For # example, to change the path to the Oh My Zsh repository: # ZSH=~/.zsh sh install.sh # # Respects the following environment variables: # ZSH - path to the Oh My Zsh repository folder (default: $HOME/.oh-my-zsh) # REPO - name of the GitHub repo to install from (default: ohmyzsh/ohmyzsh) # REMOTE - full remote URL of the git repo to install (default: GitHub via HTTPS) # BRANCH - branch to check out immediately after install (default: master) # # Other options: # CHSH - 'no' means the installer will not change the default shell (default: yes) # RUNZSH - 'no' means the installer will not run zsh after the install (default: yes) # KEEP_ZSHRC - 'yes' means the installer will not replace an existing .zshrc (default: no) # # You can also pass some arguments to the install script to set some these options: # --skip-chsh: has the same behavior as setting CHSH to 'no' # --unattended: sets both CHSH and RUNZSH to 'no' # --keep-zshrc: sets KEEP_ZSHRC to 'yes' # For example: # sh install.sh --unattended # or: # sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended # set -e # Track if $ZSH was provided custom_zsh=${ZSH:+yes} # Default settings ZSH=${ZSH:-~/.oh-my-zsh} REPO=${REPO:-ohmyzsh/ohmyzsh} REMOTE=${REMOTE:-https://github.com/${REPO}.git} BRANCH=${BRANCH:-master} # Other options CHSH=${CHSH:-yes} RUNZSH=${RUNZSH:-yes} KEEP_ZSHRC=${KEEP_ZSHRC:-no} command_exists() { command -v "$@" >/dev/null 2>&1 } fmt_error() { printf '%sError: %s%s
' "$BOLD$RED" "$*" "$RESET" >&2 } fmt_underline() { printf '[4m%s[24m
' "$*" } fmt_code() { # shellcheck disable=SC2016 # backtic in single-quote printf '`[38;5;247m%s%s`
' "$*" "$RESET" } setup_color() { # Only use colors if connected to a terminal if [ -t 1 ]; then RED=$(printf '[31m') GREEN=$(printf '[32m') YELLOW=$(printf '[33m') BLUE=$(printf '[34m') BOLD=$(printf '[1m') RESET=$(printf '[m') else RED="" GREEN="" YELLOW="" BLUE="" BOLD="" RESET="" fi } setup_ohmyzsh() { # Prevent the cloned repository from having insecure permissions. Failing to do # so causes compinit() calls to fail with "command not found: compdef" errors # for users with insecure umasks (e.g., "002", allowing group writability). Note # that this will be ignored under Cygwin by default, as Windows ACLs take # precedence over umasks except for filesystems mounted with option "noacl". umask g-w,o-w echo "${BLUE}Cloning Oh My Zsh...${RESET}" command_exists git || { fmt_error "git is not installed" exit 1 } ostype=$(uname) if [ -z "${ostype%CYGWIN*}" ] && git --version | grep -q msysgit; then fmt_error "Windows/MSYS Git is not supported on Cygwin" fmt_error "Make sure the Cygwin git package is installed and is first on the \$PATH" exit 1 fi git clone -c core.eol=lf -c core.autocrlf=false \ -c fsck.zeroPaddedFilemode=ignore \ -c fetch.fsck.zeroPaddedFilemode=ignore \ -c receive.fsck.zeroPaddedFilemode=ignore \ --depth=1 --branch "$BRANCH" "$REMOTE" "$ZSH" || { fmt_error "git clone of oh-my-zsh repo failed" exit 1 } echo } setup_zshrc() { # Keep most recent old .zshrc at .zshrc.pre-oh-my-zsh, and older ones # with datestamp of installation that moved them aside, so we never actually # destroy a user's original zshrc echo "${BLUE}Looking for an existing zsh config...${RESET}" # Must use this exact name so uninstall.sh can find it OLD_ZSHRC=~/.zshrc.pre-oh-my-zsh if [ -f ~/.zshrc ] || [ -h ~/.zshrc ]; then # Skip this if the user doesn't want to replace an existing .zshrc if [ "$KEEP_ZSHRC" = yes ]; then echo "${YELLOW}Found ~/.zshrc.${RESET} ${GREEN}Keeping...${RESET}" return fi if [ -e "$OLD_ZSHRC" ]; then OLD_OLD_ZSHRC="${OLD_ZSHRC}-$(date +%Y-%m-%d_%H-%M-%S)" if [ -e "$OLD_OLD_ZSHRC" ]; then fmt_error "$OLD_OLD_ZSHRC exists. Can't back up ${OLD_ZSHRC}" fmt_error "re-run the installer again in a couple of seconds" exit 1 fi mv "$OLD_ZSHRC" "${OLD_OLD_ZSHRC}" echo "${YELLOW}Found old ~/.zshrc.pre-oh-my-zsh." \ "${GREEN}Backing up to ${OLD_OLD_ZSHRC}${RESET}" fi echo "${YELLOW}Found ~/.zshrc.${RESET} ${GREEN}Backing up to ${OLD_ZSHRC}${RESET}" mv ~/.zshrc "$OLD_ZSHRC" fi echo "${GREEN}Using the Oh My Zsh template file and adding it to ~/.zshrc.${RESET}" sed "/^export ZSH=/ c\ export ZSH=\"$ZSH\" " "$ZSH/templates/zshrc.zsh-template" > ~/.zshrc-omztemp mv -f ~/.zshrc-omztemp ~/.zshrc echo } setup_shell() { # Skip setup if the user wants or stdin is closed (not running interactively). if [ "$CHSH" = no ]; then return fi # If this user's login shell is already "zsh", do not attempt to switch. if [ "$(basename -- "$SHELL")" = "zsh" ]; then return fi # If this platform doesn't provide a "chsh" command, bail out. if ! command_exists chsh; then cat <<EOF I can't change your shell automatically because this system does not have chsh. ${BLUE}Please manually change your default shell to zsh${RESET} EOF return fi echo "${BLUE}Time to change your default shell to zsh:${RESET}" # Prompt for user choice on changing the default login shell printf '%sDo you want to change your default shell to zsh? [Y/n]%s ' \ "$YELLOW" "$RESET" read -r opt case $opt in y*|Y*|"") echo "Changing the shell..." ;; n*|N*) echo "Shell change skipped."; return ;; *) echo "Invalid choice. Shell change skipped."; return ;; esac # Check if we're running on Termux case "$PREFIX" in *com.termux*) termux=true; zsh=zsh ;; *) termux=false ;; esac if [ "$termux" != true ]; then # Test for the right location of the "shells" file if [ -f /etc/shells ]; then shells_file=/etc/shells elif [ -f /usr/share/defaults/etc/shells ]; then # Solus OS shells_file=/usr/share/defaults/etc/shells else fmt_error "could not find /etc/shells file. Change your default shell manually." return fi # Get the path to the right zsh binary # 1. Use the most preceding one based on $PATH, then check that it's in the shells file # 2. If that fails, get a zsh path from the shells file, then check it actually exists if ! zsh=$(command -v zsh) || ! grep -qx "$zsh" "$shells_file"; then if ! zsh=$(grep '^/.*/zsh$' "$shells_file" | tail -1) || [ ! -f "$zsh" ]; then fmt_error "no zsh binary found or not present in '$shells_file'" fmt_error "change your default shell manually." return fi fi fi # We're going to change the default shell, so back up the current one if [ -n "$SHELL" ]; then echo "$SHELL" > ~/.shell.pre-oh-my-zsh else grep "^$USERNAME:" /etc/passwd | awk -F: '{print $7}' > ~/.shell.pre-oh-my-zsh fi # Actually change the default shell to zsh if ! chsh -s "$zsh"; then fmt_error "chsh command unsuccessful. Change your default shell manually." else export SHELL="$zsh" echo "${GREEN}Shell successfully changed to '$zsh'.${RESET}" fi echo } main() { # Run as unattended if stdin is not a tty if [ ! -t 0 ]; then RUNZSH=no CHSH=no fi # Parse arguments while [ $# -gt 0 ]; do case $1 in --unattended) RUNZSH=no; CHSH=no ;; --skip-chsh) CHSH=no ;; --keep-zshrc) KEEP_ZSHRC=yes ;; esac shift done setup_color if ! command_exists zsh; then echo "${YELLOW}Zsh is not installed.${RESET} Please install zsh first." exit 1 fi if [ -d "$ZSH" ]; then echo "${YELLOW}The \$ZSH folder already exists ($ZSH).${RESET}" if [ "$custom_zsh" = yes ]; then cat <<EOF You ran the installer with the \$ZSH setting or the \$ZSH variable is exported. You have 3 options: 1. Unset the ZSH variable when calling the installer: $(fmt_code "ZSH= sh install.sh") 2. Install Oh My Zsh to a directory that doesn't exist yet: $(fmt_code "ZSH=path/to/new/ohmyzsh/folder sh install.sh") 3. (Caution) If the folder doesn't contain important information, you can just remove it with $(fmt_code "rm -r $ZSH") EOF else echo "You'll need to remove it if you want to reinstall." fi exit 1 fi setup_ohmyzsh setup_zshrc setup_shell printf %s "$GREEN" cat <<'EOF' __ __ ____ / /_ ____ ___ __ __ ____ _____/ /_ / __ \/ __ \ / __ `__ \/ / / / /_ / / ___/ __ \ / /_/ / / / / / / / / / / /_/ / / /_(__ ) / / / \____/_/ /_/ /_/ /_/ /_/\__, / /___/____/_/ /_/ /____/ ....is now installed! EOF cat <<EOF Before you scream Oh My Zsh! please look over the ~/.zshrc file to select plugins, themes, and options. • Follow us on Twitter: $(fmt_underline https://twitter.com/ohmyzsh) • Join our Discord server: $(fmt_underline https://discord.gg/ohmyzsh) • Get stickers, shirts, coffee mugs and other swag: $(fmt_underline https://shop.planetargon.com/collections/oh-my-zsh) EOF printf %s "$RESET" if [ $RUNZSH = no ]; then echo "${YELLOW}Run zsh to try it out.${RESET}" exit fi exec zsh -l } main "$@"

  106  zsh config
  107  zsh -config
  108  open ~/.zshrc
  109  xcode-select --install
  110  brew install zsh
  111  echo /bin/zsh
  112  brew install git
  113  git --version
  114  brew install --cask visual-studio-code
  115  chsh -s /bin/zsh
  116  ZSH_DISABLE_COMPFIX true
  117  compaudit | xargs chmod g-w,o-w
  118  echo /bin/zsh
  119  zsh config
  120  zsh -config
  121  oh my zsh
  122  git
  123  cd
  124  ls
  125  pwd
  126  cd general assembly
  127  ls
  128  cd desktop
  129  ls
  130  cd general assembly
  131  cd General Assembly
  132  cd
  133  ls
  134  cd desktop
  135  cd desktop/General-Assembly
  136  cd
  137  ls
  138  vit --version
  139  git --version
  140  cd desktop
  141  ls
  142  cd General-assembly
  143  cd GA
  144  mkdir GA
  145  cd GA
  146  pwd
  147  open ~/.zshrc
  148  /usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/Apple/usr/bin
  149  code .
  150  code
  151  code ~/.zshrc
  152  cd desktop
  153  ls
  154  cd ga
  155  ls
  156  pwd
  157  git config --global init.defaultBranch main
  158  git config --global user.name miknayr
  159  git config --global user.email teamry4n@gmail.com
  160  git config --global push.default simple
  161  git config --global credential.helper cache
  162  ls -al ~/.ssh
  163  git config --global user.name miknayr
  164  git config --global user.email teamry4n@gmail.com
  165  git config
  166  code ~/.gitconfig
  167  ls -al ~/.ssh
  168  $ ssh-keygen -t ed25519 -C teamry4n@gmail.com
  169  ssh-keygen -t ed25519 -C teamry4n@gmail.com
  170  ls -al ~/.ssh
  171  code ~/.sshry4n1!
  172  cd /users/miknayr/.ssh
  173  cd /users/
  174  ls
  175  cd miknayr
  176  cd
  177  cd .a
  178  cd -a
  179  ls -a
  180  cd miknayr
  181  cd users/miknayr
  182  cd users
  183  cd
  184  pwd
  185  ls -a
  186  ssh-keygen -t ed25519 -C 
  187  ssh-keygen -t ed25519 -C teamry4n@gmail.com
  188  ls -al ~/.ssh
  189  rm ~/.ssh
  190  rm ~/.ssh/id_ed25519
  191  rm ~/.ssh/id_ed25519.pub
  192  ls -al ~/.ssh
  193  ssh-keygen -t ed25519 -C teamry4n@gmail.com
  194  eval SSH_AUTH_SOCK=/var/folders/hk/183pttgd7lv58c902gh2t6_00000gn/T//ssh-2HgaHmwJFha9/agent.9065; export SSH_AUTH_SOCK; SSH_AGENT_PID=9066; export SSH_AGENT_PID; echo Agent pid 9066;
  195  open ~/.sshconfig
  196  open ~/sshkeys.ssh/config
  197  touch ~/.ssh/config
  198  open ~/.ssh/config
  199  ssh-add -K ~/.ssh/id_ed25519
  200  ls -a
  201  ssh-add -K ~/.ssh/id_ed25519
  202  eval SSH_AUTH_SOCK=/var/folders/hk/183pttgd7lv58c902gh2t6_00000gn/T//ssh-KscVBqa2y3K0/agent.9067; export SSH_AUTH_SOCK; SSH_AGENT_PID=9068; export SSH_AGENT_PID; echo Agent pid 9068;
  203  cd
  204  ls
  205  mkdir .ssh
  206  ls -a
  207  cd .ssh
  208  touch ~/.ssh/config
  209  open ~/.ssh/config
  210  ssh-add -K ~/.ssh/id_ed25519
  211  touch config
  212  open config
  213  ssh-add -K ~/.ssh/id_ed25519
  214  ssh-keygen -t ed25519 -C teamry4n@gmail.com
  215  eval SSH_AUTH_SOCK=/var/folders/hk/183pttgd7lv58c902gh2t6_00000gn/T//ssh-8LokSs5inMCJ/agent.9069; export SSH_AUTH_SOCK; SSH_AGENT_PID=9070; export SSH_AGENT_PID; echo Agent pid 9070;
  216  open ~/.ssh/config
  217  touch ~/.ssh/config
  218  open ~/.ssh/config
  219  ssh-add -K ~/.ssh/id_ed25519
  220  cd
  221  pbcopy < ~/.ssh/id_ed25519.pub
  222  cde
  223  cd
  224  code ~/.zshrc
  225  ls -a
  226  pwd
  227  open .
  228  ls
  229  ls download
  230  ls downloads
  231  cd downloads
  232  clear
  233  history
  234  pwd
  235  ls
  236  cd
  237  ls
  238  pwd
  239  cd downloads
  240  cd..
  241  cd ..
  242  man
  243  man ls
  244  pwd
  245  ls -l
  246  rm sshkeys
  247  ls
  248  ls -a
  249  ls -l
  250  open ~/sshkeys.pub
  251  man ls
  252  cd ..
  253  ls
  254  cd ..
  255  cd ~
  256  ls
  257  cd ~
  258  cd downloads
  259  cd ~
  260  cd useres
  261  cd users
  262  ls
  263  cd Users
  264  ls
  265  cd ~
  266  pwd
  267  ls
  268  cd desktop
  269  ls
  270  cd ga
  271  mkdir Unit 1
  272  ls
  273  mkdir Unit 1
  274  ls
  275  desktop
  276  cd desktop
  277  pwd
  278  cd ..
  279  ..
  280  cd desktop
  281  cd ga
  282  pwd
  283  open .
  284  cd unit-1
  285  ls
  286  cd Unit 1
  287  cd ..
  288  mkdir unit 1/deliverables
  289  ls
  290  open
  291  open .
  292  touch about.txt
  293  ls
  294  cat about.txt
  295  cd
  296  ls
  297  cd ga
  298  cd desktop/ga
  299  ls
  300  cat about.txt
  301  echo hello
  302  echo hello> about.txt
  303  grep hello
  304  cat about.txt
  305  grep hello
  306  cat about.txt
  307  echo hello! this is my test file > about.txt
  308  cat about.txt
  309  grep hello
  310  cat about.txt | grep hello
  311  mkdir git-basics
  312  rm git-basics
  313  rmdir git-basics
  314  cd unit 1
  315  mkdir git basics
  316  cd git basics
  317  git init
  318  git status
  319  touch example.txt
  320  ls
  321  git status
  322  git add example.txt
  323  git status
  324  git commit -m added example.txt
  325  git status
  326  clear
  327  git log
  328  echo first change - rk >> example.txt
  329  cat example.txt
  330  echo second change -rk >> example.txt
  331  cat example.txt
  332  git diff
  333  git diff example.txt
  334  git add example.txt
  335  git status
  336  git commit -m added first and second change text to example.txt
  337  git log
  338  git checkout -review 4c00a
  339  git log -review 4c00a
  340  git log -review commit history
  341  git diff 4c00a
  342  git diff
  343  git status
  344  git status example.txt
  345  git checkout
  346  cd ..
  347  mkdir tacos
  348  cd tacos
  349  echo # tacos >> README.md
git init
git add README.md
git commit -m first commit
git branch -M main
git remote add origin https://github.com/miknayr/tacos.git
git push -u origin main
  350  cat README.md
  351  echo i love tacos
