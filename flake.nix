{
  description = "Truc";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let pkgs = import nixpkgs {
        config = { allowUnfree = true; };
        inherit system;
      };
      in
      {
        devShell = pkgs.mkShell {
          buildInputs = [
            (pkgs.python312.withPackages (ps: [
              # build dep

              # dev dep
              ps.black
              ps.pylint
              ps.ipython
              ps.python-lsp-server
            ]))
          ];
        };
      });
}

