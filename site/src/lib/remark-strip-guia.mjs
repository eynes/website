import { remove } from 'unist-util-remove';

/**
 * Strips internal editorial `<!-- GUÍA: ... -->` HTML comments (and the
 * generic `<!-- ... -->` wrapper comments used the same way in some files)
 * from Markdown content before it renders. These comments are meant only
 * for whoever writes/maintains content/ and must never reach production HTML.
 */
export function stripGuiaComments() {
  return (tree) => {
    remove(tree, (node) => node.type === 'html' && /^<!--/.test(node.value ?? ''));
  };
}
