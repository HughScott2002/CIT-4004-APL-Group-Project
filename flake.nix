{
  description = "TypeSnake - A statically-typed functional programming language";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    flake-compat = {
      url = "github:edolstra/flake-compat";
      flake = false;
    };
  };

  outputs = { self, nixpkgs, flake-utils, flake-compat }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        pythonEnv = pkgs.python312.withPackages (ps: with ps; [
          flask
          flask-cors
          gunicorn
          ply
          pytest
          setuptools
          pip
        ]);
      in {
        devShells.default = pkgs.mkShell {
          buildInputs = [ pythonEnv ];
          nativeBuildInputs = with pkgs; [ ruff ];

          shellHook = ''
            export PYTHONPATH="${self}/src:$PYTHONPATH"
            echo "TypeSnake dev shell ready."
            echo "  python: $(python --version)"
            echo "  ruff:   $(ruff --version 2>/dev/null | head -1)"
            echo ""
            echo "  server:   python server/main.py"
            echo "  cli:      python server/app.py"
            echo "  lint:     ruff check src/ server/"
            echo "  test:     pytest"
            echo "  editable: pip install -e ."
          '';
        };
      });
}
