### JOURNAL

This is a small set of tools that attempts to become a open source journaling alternative for people who don't trust other products that are available where you upload your notes to some servers and trust that these companies keep it secure.

The main difference about this tool is that everything is encrypted with your own encryption key. Of course creating new ones can be a bit hard, therefore there is also a script to generate a key based on a passphrase that the user might choose. This key generation tool is not mandatory for the encryption and decryption of files, therefore nobody is forced to use that key generation, it is ultimately for convenience to some of the users.

The ultimate goal is also to add some more automatic steps, so overall this tool can be closed and anyone can start using it in a private or even public repository. Git is good at versioning so it could be quite nice to have also some hooks, so that files inside the __./content__ folder are encrypted before commiting it to Git. Therefore some integrations with git-hooks will also be implemented.



## TODO:
 * --There should be still one tool to rule it all, therefore you can even do the key generation, then also encrypting the files.--
 * There should also be a scrupt to encrypt each file inside of ./content folder automatically.
 * It is missing a git-hook to encrypt the files that are decrypted into git, so that no file inside the ./content folder is commited and pushed while in plain-text.
