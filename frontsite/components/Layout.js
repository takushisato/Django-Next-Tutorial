import Head from 'next/head'
import Navigation from './Navigation'

const Layout = (props) => {
    return(
        <>
            <Head>
                <meta name='viewport' content="width=device-width, initial-scale=1" />
            </Head>
            <Navigation />
            <div className='px-8 py-6 mx-auto max-w-7xl'>{props.childlen}</div>
        </>
    )
}

export default Layout