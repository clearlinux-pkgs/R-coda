#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-coda
Version  : 0.19.4
Release  : 35
URL      : https://cran.r-project.org/src/contrib/coda_0.19-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/coda_0.19-4.tar.gz
Summary  : Output Analysis and Diagnostics for MCMC
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R

%description
output from Markov Chain Monte Carlo (MCMC) simulations, as
	well as diagnostic tests of convergence to the equilibrium
	distribution of the Markov chain.

%prep
%setup -q -c -n coda
cd %{_builddir}/coda

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1601568889

%install
export SOURCE_DATE_EPOCH=1601568889
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library coda
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library coda
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library coda
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc coda || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/coda/AUTHORS
/usr/lib64/R/library/coda/CITATION
/usr/lib64/R/library/coda/DESCRIPTION
/usr/lib64/R/library/coda/INDEX
/usr/lib64/R/library/coda/Meta/Rd.rds
/usr/lib64/R/library/coda/Meta/data.rds
/usr/lib64/R/library/coda/Meta/features.rds
/usr/lib64/R/library/coda/Meta/hsearch.rds
/usr/lib64/R/library/coda/Meta/links.rds
/usr/lib64/R/library/coda/Meta/nsInfo.rds
/usr/lib64/R/library/coda/Meta/package.rds
/usr/lib64/R/library/coda/NAMESPACE
/usr/lib64/R/library/coda/R/coda
/usr/lib64/R/library/coda/R/coda.rdb
/usr/lib64/R/library/coda/R/coda.rdx
/usr/lib64/R/library/coda/data/line.rda
/usr/lib64/R/library/coda/help/AnIndex
/usr/lib64/R/library/coda/help/aliases.rds
/usr/lib64/R/library/coda/help/coda.rdb
/usr/lib64/R/library/coda/help/coda.rdx
/usr/lib64/R/library/coda/help/paths.rds
/usr/lib64/R/library/coda/html/00Index.html
/usr/lib64/R/library/coda/html/R.css
