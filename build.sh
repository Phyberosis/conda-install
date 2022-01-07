PYPI=testpypi
# PYPI=pypi
TOKEN=`cat credentials/${PYPI}`

for arg in "$@"; do
    case $arg in
    --upload | -u)
        python -m twine upload --repository $PYPI pip/package/dist/* -u __token__ -p $TOKEN
        ;;

    --build | -b)
        cd pip/package
        python -m build
        ;;
    
    --conda | -c)
        conda build -c conda-forge conda/
        ;;

    *)
        echo "ignoring unknown option [$arg]"
        ;;
    esac
done