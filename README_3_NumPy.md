
readme = '''# numpy-cheat-sheet
A practical, well-organized "NumPy cheat sheet" covering array creation, indexing, broadcasting, ufuncs, linear algebra, random sampling, Fourier transforms, string operations, masked arrays, memory layout, and modern NumPy 2.x features.


# NumPy Cheat Sheet for Data Scientists, Engineers, and Developers

A practical, well-organized **NumPy cheat sheet** covering array creation, data types, indexing, slicing, broadcasting, universal functions (ufuncs), aggregation, sorting, searching, linear algebra, random sampling, discrete Fourier transforms, string operations, masked arrays, memory layout, structured arrays, polynomial fitting, histograms, and modern NumPy 2.x features.

This repository is designed for data science students, machine learning practitioners, scientific computing engineers, bootcamp learners, and anyone preparing for technical interviews who wants a fast, searchable, real-world NumPy reference with corrected syntax examples and logically grouped query patterns.

## Contributing

Contributions are welcome if you want to improve examples, fix syntax, expand coverage, or add more real-world scientific computing use cases.

## Why this NumPy Cheat Sheet?

If you are learning Python for data science, machine learning, scientific computing, image processing, or technical interviews, this project gives you a single place to review the most useful NumPy commands and patterns.

It focuses on:
- Modern NumPy-first syntax (1.x through 2.x)
- Clear examples you can reuse quickly
- Logical grouping by topic
- Short explanations for fast scanning
- Common interview and day-to-day array operations
- Cleanup of mixed or outdated syntax from broader references
- NumPy 2.0 API changes (array_api, new string dtype, copy behavior)

## What\'s Included

This NumPy cheat sheet includes:

- `np.array`, `np.ndarray` creation from lists, tuples, ranges, and files
- Special arrays: `zeros`, `ones`, `empty`, `full`, `eye`, `identity`, `diag`
- Ranges and grids: `arange`, `linspace`, `logspace`, `geomspace`, `meshgrid`, `ogrid`, `mgrid`
- Data types: `int8`–`int64`, `uint8`–`uint64`, `float16`–`float128`, `complex64`–`complex256`, `bool_`, `object_`, `str_`, `bytes_`, `StringDType` (2.0+)
- Indexing and slicing: basic, boolean, fancy, `np.where`, `np.select`, `np.clip`, `np.put`, `np.take`
- Broadcasting rules and `np.broadcast_to`, `np.broadcast_arrays`, `np.expand_dims`
- Universal functions (ufuncs): `add`, `subtract`, `multiply`, `divide`, `power`, `sqrt`, `exp`, `log`, `sin`, `cos`, `tan`, `arcsin`, `arccos`, `arctan`, `hypot`, `degrees`, `radians`, `sign`, `abs`, `fabs`, `ceil`, `floor`, `trunc`, `round`, `mod`, `remainder`, `divmod`, `maximum`, `minimum`, `fmax`, `fmin`, `copysign`, `nextafter`, `spacing`, `ldexp`, `frexp`, `modf`, `isfinite`, `isinf`, `isnan`, `isnat`, `signbit`, `less`, `less_equal`, `greater`, `greater_equal`, `equal`, `not_equal`, `logical_and`, `logical_or`, `logical_xor`, `logical_not`
- Aggregation: `sum`, `prod`, `mean`, `std`, `var`, `min`, `max`, `argmin`, `argmax`, `median`, `percentile`, `quantile`, `average`, `nanmean`, `nansum`, `nanstd`, `nanvar`, `nanmin`, `nanmax`, `nanargmin`, `nanargmax`, `nanmedian`, `nanpercentile`, `nanquantile`
- Cumulative operations: `cumsum`, `cumprod`, `cumulative_sum` (2.0), `nancumsum`, `nancumprod`, `diff`, `ediff1d`, `gradient`, `trapz`, `cross`, `inner`, `outer`, `tensordot`, `einsum`, `vdot`, `matmul`, `@` operator
- Sorting and searching: `sort`, `argsort`, `lexsort`, `partition`, `argpartition`, `searchsorted`, `argwhere`, `nonzero`, `flatnonzero`, `count_nonzero`, `extract`, `unique`, `intersect1d`, `union1d`, `setdiff1d`, `setxor1d`, `in1d`, `isin`
- Shape manipulation: `reshape`, `ravel`, `flatten`, `transpose`, `swapaxes`, `moveaxis`, `rollaxis`, `squeeze`, `expand_dims`, `atleast_1d`, `atleast_2d`, `atleast_3d`, `stack`, `vstack`, `hstack`, `dstack`, `column_stack`, `row_stack`, `concatenate`, `append`, `tile`, `repeat`, `split`, `hsplit`, `vsplit`, `dsplit`, `array_split`, `unravel_index`, `ravel_multi_index`
- Linear algebra (`np.linalg`): `dot`, `matmul`, `matrix_power`, `det`, `slogdet`, `inv`, `pinv`, `solve`, `lstsq`, `eig`, `eigvals`, `eigh`, `eigvalsh`, `svd`, `norm`, `cond`, `matrix_rank`, `qr`, `cholesky`, `tensorinv`, `tensorsolve`, `cross`, `outer`, `inner`, `kron`, `vecdot` (2.0), `matrix_norm` (2.0), `vector_norm` (2.0)
- Random sampling (`np.random`): `rand`, `randn`, `randint`, `random`, `choice`, `shuffle`, `permutation`, `normal`, `uniform`, `binomial`, `poisson`, `exponential`, `gamma`, `beta`, `seed`, `default_rng`, `Generator`, `PCG64`, `MT19937`, `integers`, `random`, `standard_normal`, `multivariate_normal`, `permuted`
- Discrete Fourier transforms (`np.fft`): `fft`, `ifft`, `fft2`, `ifft2`, `fftn`, `ifftn`, `rfft`, `irfft`, `rfft2`, `irfft2`, `rfftn`, `irfftn`, `fftshift`, `ifftshift`, `fftfreq`, `rfftfreq`
- String operations (`np.strings`, `np.char`): `add`, `multiply`, `mod`, `capitalize`, `center`, `encode`, `decode`, `join`, `ljust`, `lower`, `lstrip`, `partition`, `replace`, `rjust`, `rpartition`, `rsplit`, `rstrip`, `split`, `splitlines`, `strip`, `swapcase`, `title`, `translate`, `upper`, `zfill`, `equal`, `not_equal`, `greater`, `greater_equal`, `less`, `less_equal`, `count`, `find`, `rfind`, `index`, `rindex`, `isalpha`, `isdecimal`, `isdigit`, `islower`, `isspace`, `istitle`, `isupper`, `startswith`, `endswith`, `str_len`
- Masked arrays (`np.ma`): `masked_array`, `masked_where`, `masked_greater`, `masked_less`, `masked_inside`, `masked_outside`, `masked_invalid`, `masked_equal`, `masked_not_equal`, `masked_values`, `masked_print_option`, `filled`, `compress`, `average`, `median`, `std`, `var`, `sum`, `product`, `cumsum`, `cumprod`, `mean`, `min`, `max`, `argmin`, `argmax`, `count`, `getmask`, `getmaskarray`, `masked`, `nomask`, `fix_invalid`, `masked_all`, `masked_all_like`
- Memory layout: `flags`, `strides`, `itemsize`, `nbytes`, `base`, `data`, `ctypes`, `view`, `copy`, `deepcopy`, `ascontiguousarray`, `asfortranarray`, `require`, `share_memory`
- Structured arrays: `dtype`, `recarray`, `fromarrays`, `fromrecords`, `fromfile`, `tofile`, `save`, `load`, `savez`, `savez_compressed`, `memmap`
- Polynomial fitting (`np.polynomial`): `Polynomial`, `Chebyshev`, `Legendre`, `Hermite`, `Laguerre`, `polyfit`, `polyval`, `polyder`, `polyint`, `roots`, `fit`
- Histograms and binning: `histogram`, `histogram2d`, `histogramdd`, `bincount`, `digitize`, `searchsorted`
- Set operations: `unique`, `intersect1d`, `union1d`, `setdiff1d`, `setxor1d`, `in1d`, `isin`
- Testing and assertions: `allclose`, `isclose`, `array_equal`, `array_equiv`, `assert_allclose`, `assert_array_equal`, `assert_array_almost_equal`
- NumPy 2.0 changes: `copy` keyword, `StringDType`, `vecdot`, `matrix_norm`, `vector_norm`, `cumulative_sum`, `cumulative_prod`, `array_api` namespace

## Who This Repository Is For

This repository is useful for:

- Data science students learning NumPy and Python
- Machine learning practitioners working with tensors and arrays
- Bootcamp students building portfolio projects
- Scientific computing engineers preparing for interviews
- Anyone converting generic Python notes into valid, up-to-date NumPy syntax



---

## Main Topics

### 1. Import & Setup
Core imports, version checks, and global configuration.

### 2. Array Creation
Creating `ndarray` objects from lists, tuples, ranges, special values, and files.

### 3. Data Types (dtypes)
Integer, unsigned integer, floating-point, complex, boolean, object, string, bytes, and custom structured dtypes.

### 4. Array Attributes & Inspection
Shape, dimensions, size, memory usage, flags, strides, and data buffer access.

### 5. Indexing & Slicing
Basic indexing, boolean masking, fancy/indexing, `np.where`, `np.select`, `np.clip`, `np.put`, `np.take`.

### 6. Broadcasting
Broadcasting rules, `np.broadcast_to`, `np.broadcast_arrays`, `np.expand_dims`, `np.newaxis`.

### 7. Universal Functions (ufuncs)
Arithmetic, trigonometric, hyperbolic, exponential, logarithmic, comparison, logical, bitwise, and floating-point ufuncs.

### 8. Aggregation & Statistics
Sum, product, mean, std, var, min, max, argmin, argmax, median, percentile, quantile, and NaN-aware variants.

### 9. Cumulative & Differential Operations
Cumsum, cumprod, diff, gradient, cross product, inner/outer product.

### 10. Sorting & Searching
Sort, argsort, partition, searchsorted, argwhere, nonzero, unique, set operations.

### 11. Shape Manipulation
Reshape, ravel, transpose, swapaxes, squeeze, expand_dims, stack, concatenate, split, tile, repeat.

### 12. Linear Algebra (np.linalg)
Matrix multiplication, decomposition, eigenvalues, SVD, norms, solving systems, determinants, inverses, and NumPy 2.0 additions.

### 13. Random Sampling (np.random)
Legacy and Generator API: rand, randn, randint, choice, shuffle, normal, uniform, binomial, poisson, seed, default_rng, PCG64.

### 14. Discrete Fourier Transforms (np.fft)
1D, 2D, N-D FFT and inverse, real FFT, frequency bins, shifting.

### 15. String Operations (np.strings / np.char)
Vectorized string manipulation, comparison, searching, splitting, joining, casing, padding.

### 16. Masked Arrays (np.ma)
Creating, masking, filling, and computing with masked arrays.

### 17. Memory Layout & Views
Contiguous arrays, Fortran order, views vs copies, memory sharing, `require`.

### 18. Structured Arrays & Records
Custom dtypes, record arrays, reading/writing binary data, memory mapping.

### 19. Polynomial Fitting (np.polynomial)
Fitting, evaluating, differentiating, integrating, finding roots of polynomials.

### 20. Histograms & Binning
Histogram, 2D histogram, N-D histogram, bincount, digitize.

### 21. Set Operations
Unique, intersection, union, difference, symmetric difference, membership testing.

### 22. Testing & Assertions
Allclose, isclose, array_equal, array_equiv, and pytest-style assertions.

### 23. Input/Output
Save, load, savez, memmap, text files, CSV, and binary I/O.

### 24. NumPy 2.0 Modern Features
StringDType, copy keyword changes, cumulative_sum, vecdot, matrix_norm, vector_norm, array_api namespace.