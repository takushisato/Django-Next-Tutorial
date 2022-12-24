import Link from 'next/link'

const Navigation = () => {
    return(
        <>
        <div className='bg-gray-900'>
            <div className='px-8 py-6 mx-auto max-w-7xl'>
                <div className='flex items-center justify-between'>
                    <div>
                        <Link>
                            <a href="/" className='text-lg font-extrabold text-white hover:text-gray-50'>
                                タイトル
                            </a>
                        </Link>
                    </div>
                </div>
            </div>
        </div>
        </>
    )
}

export default Navigation